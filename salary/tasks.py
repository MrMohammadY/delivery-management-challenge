from celery import shared_task
import datetime
from salary.models import WeeklySalary


@shared_task()
def calculate_weekly_salary():
    today = datetime.date.today()
    saturday = today - datetime.timedelta(days=6)
    if today.strftime('%a') == 'Fri' and saturday.strftime('%a') == 'Sat':
        WeeklySalary.save_weekly_salary_per_user(saturday, today)
