from django.db import models

from core.models import TimeStampedModel


class BaseTransaction(TimeStampedModel):
    class Meta:
        abstract = True

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, default='')
