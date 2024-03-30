from django.db import models


class PhoneStatus(models.TextChoices):
    BOUGHT = "Bought"
    IN_TRANSIT = "In Transit"
    IN_PROGRESS = "In Progress"
    PENDING_SALE = "Pending Sale"
    SOLD = "Sold"
    ERROR = "Error"


class Phone(models.Model):
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
