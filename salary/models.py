from django.db import models
from django.utils.translation import ugettext_lazy as _

from courser.models import Courier
from lib.model import BaseModel


class RewardDeduction(BaseModel):
    REWARD = 0
    DEDUCTION = 1
    TYPE = (
        (REWARD, _('reward')),
        (DEDUCTION, _('deduction'))
    )
    courier = models.ForeignKey(Courier, verbose_name='reward_deductions', on_delete=models.PROTECT)
    type = models.PositiveSmallIntegerField(choices=TYPE, verbose_name=_('type'))
    reason = models.CharField(max_length=120, verbose_name=_('reason'))
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name=_('price'))

    def __str__(self):
        return f'{self.get_type_display()} - {self.courier} - {self.price}'

    class Meta:
        verbose_name = _('reward deduction')
        verbose_name_plural = _('reward deductions')
        db_table = 'reward_deduction'


class DailySalary(models.Model):
    courier = models.ForeignKey(Courier, verbose_name='daily_salaries', on_delete=models.PROTECT)
    date = models.DateField(verbose_name=_('date'))
    daily_balance = models.DecimalField(max_digits=9, decimal_places=0,verbose_name=_('price'))

    def __str__(self):
        return f'{self.courier} - {self.date} - {self.daily_balance}'

    class Meta:
        verbose_name = _('daily salary')
        verbose_name_plural = _('daily salaries')
        db_table = 'daily_salary'


class WeeklySalary(models.Model):
    courier = models.ForeignKey(Courier, verbose_name='weekly_salaries', on_delete=models.PROTECT)
    from_date = models.DateField(verbose_name=_('from date'))
    to_date = models.DateField(verbose_name=_('to date'))
    weekly_balance = models.DecimalField(max_digits=9, decimal_places=0,verbose_name=_('price'))

    def __str__(self):
        return f'{self.courier} - {self.from_date} | {self.to_date} - {self.weekly_balance}'

    class Meta:
        verbose_name = _('weekly salary')
        verbose_name_plural = _('weekly salaries')
        db_table = 'weekly_salary'
