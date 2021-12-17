from django.db import models, transaction
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.utils.translation import ugettext_lazy as _

from courier.models import Courier
from lib.model import BaseModel


class RewardDeduction(BaseModel):
    REWARD = 0
    DEDUCTION = 1
    TYPE = (
        (REWARD, _('reward')),
        (DEDUCTION, _('deduction'))
    )
    courier = models.ForeignKey(
        Courier,
        related_name='reward_deductions',
        on_delete=models.PROTECT,
        verbose_name=_('courier')
    )
    type = models.PositiveSmallIntegerField(choices=TYPE, verbose_name=_('type'))
    reason = models.CharField(max_length=120, verbose_name=_('reason'))
    description = models.TextField()
    price = models.IntegerField(verbose_name=_('price'))

    def __str__(self):
        return f'{self.get_type_display()} - {self.courier} - {self.price}'

    class Meta:
        verbose_name = _('reward deduction')
        verbose_name_plural = _('reward deductions')
        db_table = 'reward_deduction'


class DailySalary(BaseModel):
    courier = models.ForeignKey(
        Courier,
        related_name='daily_salaries',
        on_delete=models.PROTECT,
        verbose_name=_('courier')
    )
    date = models.DateField(verbose_name=_('date'))
    daily_balance = models.IntegerField(verbose_name=_('price'))

    @classmethod
    def calculate_weekly_salary(cls, from_date, to_date):
        return cls.objects.filter(date__gte=from_date, date__lte=to_date).values('courier').annotate(
            weekly_balance=Coalesce(Sum('daily_balance'), 0))

    def __str__(self):
        return f'{self.courier} - {self.date} - {self.daily_balance}'

    class Meta:
        verbose_name = _('daily salary')
        verbose_name_plural = _('daily salaries')
        db_table = 'daily_salary'
        unique_together = ('courier', 'date')


class WeeklySalary(BaseModel):
    courier = models.ForeignKey(
        Courier,
        related_name='weekly_salaries',
        on_delete=models.PROTECT,
        verbose_name=_('courier')
    )
    from_date = models.DateField(verbose_name=_('from date'))
    to_date = models.DateField(verbose_name=_('to date'))
    weekly_balance = models.IntegerField(verbose_name=_('price'))

    @classmethod
    def save_weekly_salary_per_user(cls, from_date, to_date):
        weekly_salaries = DailySalary.calculate_weekly_salary(from_date, to_date)
        with transaction.atomic():
            for item in weekly_salaries:
                cls.objects.get_or_create(
                    courier=Courier.objects.get(pk=item.get('courier')),
                    from_date=from_date,
                    to_date=to_date,
                    weekly_balance=item.get('weekly_balance')
                )

    def __str__(self):
        return f'{self.courier} - {self.from_date} | {self.to_date} - {self.weekly_balance}'

    class Meta:
        verbose_name = _('weekly salary')
        verbose_name_plural = _('weekly salaries')
        db_table = 'weekly_salary'
        unique_together = ('courier', 'from_date', 'to_date')
