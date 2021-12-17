from django.urls import path, register_converter

from salary.api.utils import DateConverter
from salary.api.views import WeeklySalaryListAPIView

register_converter(DateConverter, 'date_convert')

app_name = 'api'
urlpatterns = [
    path(
        'weekly/<date_convert:from_date>/<date_convert:to_date>/',
        WeeklySalaryListAPIView.as_view(),
        name='weekly-salary'
    ),
]
