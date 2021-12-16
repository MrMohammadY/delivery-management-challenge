from django.contrib import admin

from salary.models import RewardDeduction, WeeklySalary, DailySalary


@admin.register(RewardDeduction)
class RewardDeductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'courier', 'type', 'reason', 'description', 'price')
    list_filter = ('type', )


@admin.register(DailySalary)
class DailySalaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'courier', 'date', 'daily_balance')


@admin.register(WeeklySalary)
class WeeklySalaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'courier', 'from_date', 'to_date', 'weekly_balance')
