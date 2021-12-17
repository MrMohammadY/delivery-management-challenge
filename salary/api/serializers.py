from rest_framework import serializers

from salary.models import WeeklySalary
from courier.models import Courier


class NestedCourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ('id', 'first_name', 'last_name')


class WeeklySalarySerializer(serializers.ModelSerializer):
    courier = NestedCourierSerializer()

    class Meta:
        model = WeeklySalary
        fields = ('courier', 'from_date', 'to_date', 'weekly_balance')
