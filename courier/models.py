from django.db import models
from django.db.models import Sum, Q
from django.db.models.functions import Coalesce
from django.utils.translation import ugettext_lazy as _


class Courier(models.Model):
    first_name = models.CharField(max_length=30, verbose_name=_('first name'))
    last_name = models.CharField(max_length=40, verbose_name=_('last name'))

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    def total_balance_trip_per_day(self, date):
        return self.trips.filter(created_time=date).aggregate(total_balance=Sum('price'))

    def total_balance_reward_deduction_per_day(self, date):
        from salary.models import RewardDeduction
        reward_transactions = Sum('price', filter=Q(type=RewardDeduction.REWARD))
        deduction_transactions = Sum('price', filter=Q(type=RewardDeduction.DEDUCTION))
        return self.reward_deductions.filter(created_time=date).aggregate(
            total_balance=Coalesce(reward_transactions, 0) - Coalesce(deduction_transactions, 0)
        )

    def calculate_total_balance_per_day(self, date):
        balance_trip = self.total_balance_trip_per_day(date).get('total_balance')
        balance_reward_deduction = self.total_balance_reward_deduction_per_day(date).get('total_balance')
        return balance_trip + balance_reward_deduction

    class Meta:
        verbose_name = _('courier')
        verbose_name_plural = _('couriers')
        db_table = 'courier'
