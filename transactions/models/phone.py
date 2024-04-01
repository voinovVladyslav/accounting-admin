from django.db import models

from .base import BaseTransaction


class PhoneTransaction(BaseTransaction):
    class Meta:
        verbose_name = 'Phone Transaction'
        verbose_name_plural = 'Phone Transactions'

    phone = models.ForeignKey(
        'phones.Phone',
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    def __str__(self):
        return f'{self.phone} - {self.amount}'
