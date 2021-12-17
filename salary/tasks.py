from celery import shared_task
import datetime
from salary.models import WeeklySalary


@shared_task()
def calculate_weekly_salary():
    today = datetime.date.today()
    friday = today - datetime.timedelta(days=1)
    saturday = today - datetime.timedelta(days=7)
    if friday.strftime('%a') == 'Fri' and saturday.strftime('%a') == 'Sat':
        WeeklySalary.save_weekly_salary_per_user(saturday, friday)
