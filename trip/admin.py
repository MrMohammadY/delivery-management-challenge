from django.contrib import admin

from trip.models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'courier', 'start_time', 'end_time', 'price', 'created_time', 'modified_time')
