from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from salary.models import RewardDeduction, DailySalary
from trip.models import Trip

from datetime import datetime


@receiver(post_save, sender=RewardDeduction)
@receiver(post_save, sender=Trip)
def callback(sender, instance, created, **kwargs):
    with transaction.atomic():
        date = datetime.today().strftime('%Y-%m-%d')
        DailySalary.objects.update_or_create(
            courier=instance.courier,
            date=instance.created_time,
            defaults={
                'daily_balance': instance.courier.calculate_total_balance_per_day(date)
            }
        )
