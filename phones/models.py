from django.db import models

from core.models import TimeStampedModel


class PhoneStatus(models.TextChoices):
    BOUGHT = "Bought"
    IN_TRANSIT = "In Transit"
    IN_PROGRESS = "In Progress"
    PENDING_SALE = "Pending Sale"
    SOLD = "Sold"
    ERROR = "Error"


class Phone(TimeStampedModel):
    name = models.CharField(
        max_length=200,
    )
    imei = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="IMEI",
    )
    estimated_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    status = models.CharField(
        max_length=50,
        choices=PhoneStatus.choices,
        default=PhoneStatus.BOUGHT,
    )

    def __str__(self):
        return f'{self.name} ({self.imei})'


class PhonePart(TimeStampedModel):
    class Meta:
        verbose_name = "Phone Part"
        verbose_name_plural = "Phone Parts"

    name = models.CharField(
        max_length=200,
    )
    phone = models.ForeignKey(
        Phone,
        on_delete=models.CASCADE,
        related_name="parts",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name} ({self.pk})'
