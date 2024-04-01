from django.db import models

from .base import BaseTransaction


class PhonePartTransaction(BaseTransaction):
    class Meta:
        verbose_name = 'Phone Part Transaction'
        verbose_name_plural = 'Phone Part Transactions'

    phone_part = models.ForeignKey(
        'phones.PhonePart',
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    def __str__(self):
        return f'{self.phone_part} - {self.amount}'
