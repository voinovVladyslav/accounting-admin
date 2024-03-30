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

    def __str__(self):
        return f'{self.name} ({self.imei})'


class PhonePart(models.Model):
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
    )

    def __str__(self):
        return f'{self.name} ({self.pk})'

