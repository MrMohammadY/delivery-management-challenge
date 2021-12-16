from django.contrib import admin

from courser.models import Courier


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

