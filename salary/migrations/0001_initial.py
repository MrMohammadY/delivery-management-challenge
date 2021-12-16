# Generated by Django 3.2 on 2021-12-16 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklySalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(verbose_name='from date')),
                ('to_date', models.DateField(verbose_name='to date')),
                ('weekly_balance', models.IntegerField(verbose_name='price')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courier.courier', verbose_name='weekly_salaries')),
            ],
            options={
                'verbose_name': 'weekly salary',
                'verbose_name_plural': 'weekly salaries',
                'db_table': 'weekly_salary',
            },
        ),
        migrations.CreateModel(
            name='RewardDeduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateField(auto_now=True, verbose_name='created time')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'reward'), (1, 'deduction')], verbose_name='type')),
                ('reason', models.CharField(max_length=120, verbose_name='reason')),
                ('description', models.TextField()),
                ('price', models.IntegerField(verbose_name='price')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reward_deductions', to='courier.courier', verbose_name='courier')),
            ],
            options={
                'verbose_name': 'reward deduction',
                'verbose_name_plural': 'reward deductions',
                'db_table': 'reward_deduction',
            },
        ),
        migrations.CreateModel(
            name='DailySalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('daily_balance', models.IntegerField(verbose_name='price')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courier.courier', verbose_name='daily_salaries')),
            ],
            options={
                'verbose_name': 'daily salary',
                'verbose_name_plural': 'daily salaries',
                'db_table': 'daily_salary',
                'unique_together': {('courier', 'date')},
            },
        ),
    ]
