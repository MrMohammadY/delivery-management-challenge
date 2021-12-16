from django.db import models, transaction
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _

from courier.models import Courier

from lib.model import BaseModel


class Trip(BaseModel):
    courier = models.ForeignKey(Courier, related_name='trips', on_delete=models.PROTECT, verbose_name=_('courier'))
    start_time = models.TimeField(auto_now_add=True, verbose_name=_('start time'))
    end_time = models.TimeField(blank=True, null=True, verbose_name=_('end time'))
    price = models.IntegerField(verbose_name=_('price'))

    def __str__(self):
        return f'{self.courier} (start time:{self.start_time} end time:{self.end_time}) cost:{self.price}'

    class Meta:
        verbose_name = _('trip')
        verbose_name_plural = _('trips')
        db_table = 'trip'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        with transaction.atomic():
            super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    @classmethod
    def total_balance_per_day(cls, courier_id, date):
        return cls.objects.filter(courier=courier_id, created_time=date).aggregate(total_balance=Sum('price'))
