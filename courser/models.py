from django.db import models
from django.utils.translation import ugettext_lazy as _


class Courier(models.Model):
    first_name = models.CharField(max_length=30, verbose_name=_('last name'))
    last_name = models.CharField(max_length=40, verbose_name=_('last name'))

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('courier')
        verbose_name_plural = _('couriers')
        db_table = 'courier'
