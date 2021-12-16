from django.db import models
from django.utils.translation import ugettext_lazy as _

from courser.models import Courier

from lib.model import BaseModel


class Trip(BaseModel):
    courier = models.ForeignKey(Courier, related_name='trips', on_delete=models.PROTECT, verbose_name=_('courier'))
    start_time = models.TimeField(auto_now_add=True, verbose_name=_('start time'))
    end_time = models.TimeField(blank=True, null=True, verbose_name=_('end time'))
    price = models.DecimalField(max_digits=6, decimal_places=0, verbose_name=_('price'))

    def __str__(self):
        return f'{self.courier} (start time:{self.start_time} end time:{self.end_time}) cost:{self.price}'

    class Meta:
        verbose_name = _('trip')
        verbose_name_plural = _('trips')
        db_table = 'trip'
