from django.db import models
from django.contrib.auth import get_user_model

from .base import BaseTransaction


class UserTransaction(BaseTransaction):
    class Meta:
        verbose_name = 'User Transaction'
        verbose_name_plural = 'User Transactions'

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    def __str__(self):
        return f'{self.user} - {self.amount}'
