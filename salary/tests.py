from django.test import TestCase
from datetime import date
from courier.models import Courier
from trip.models import Trip
from salary.models import DailySalary, RewardDeduction


class DailySalaryTestCase(TestCase):
    def setUp(self):
        self.courier = Courier.objects.create(first_name='first name test', last_name='last name test')
        self.today = date.today()

    @property
    def salary(self):
        return DailySalary.objects.get(courier=self.courier, date=self.today)

    def test_correct_calculate_daily_balance(self):
        trip_1 = Trip.objects.create(courier=self.courier, price=25000)
        self.assertEqual(self.salary.daily_balance, trip_1.price)

        trip_2 = Trip.objects.create(courier=self.courier, price=22000)
        self.assertEqual(self.salary.daily_balance, trip_1.price + trip_2.price)

        trip_2.price = 42000
        trip_2.save()
        self.assertEqual(self.salary.daily_balance, trip_1.price + trip_2.price)

        reward_1 = RewardDeduction.objects.create(
            courier=self.courier,
            type=RewardDeduction.REWARD,
            reason='Reward for timely delivery',
            description='...', price=5000
        )
        self.assertEqual(self.salary.daily_balance, trip_1.price + trip_2.price + reward_1.price)

        deduction_1 = RewardDeduction.objects.create(
            courier=self.courier,
            type=RewardDeduction.DEDUCTION,
            reason='Deduction for bad post',
            description='...',
            price=3000
        )
        self.assertEqual(self.salary.daily_balance, trip_1.price + trip_2.price + reward_1.price - deduction_1.price)

        deduction_1.price = 12000
        deduction_1.save()
        self.assertEqual(self.salary.daily_balance, trip_1.price + trip_2.price + reward_1.price - deduction_1.price)
