from django.db import transaction
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver

from salary.models import RewardDeduction, DailySalary
from trip.models import Trip

from datetime import date as date_today


@receiver(post_save, sender=RewardDeduction)
@receiver(post_save, sender=Trip)
def callback(sender, instance, created, **kwargs):
    if created or instance.before_change_price != instance.price:
        with transaction.atomic():
            date = date_today.today()
            DailySalary.objects.update_or_create(
                courier=instance.courier,
                date=instance.created_time,
                defaults={
                    'daily_balance': instance.courier.calculate_total_balance_per_day(instance.created_time.date())
                }
            )


@receiver(post_init, sender=RewardDeduction)
@receiver(post_init, sender=Trip)
def store_change_price(sender, instance, **kwargs):
    instance.before_change_price = instance.price
