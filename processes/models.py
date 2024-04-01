from django.db import models
from django.db.models.functions import Lower
from django.utils import timezone


class ProcessStatus(models.TextChoices):
    CREATED = 'Created'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    ERROR = 'Error'


class ProcessType(models.Model):
    class Meta:
        verbose_name = 'Process Type'
        verbose_name_plural = 'Process Types'
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='unique_process_type_name',
            ),
        ]

    name = models.CharField(
        max_length=200,
    )
    description = models.TextField(
        blank=True,
        default='',
    )

    def __str__(self):
        return f'{self.name}'


class Process(models.Model):
    class Meta:
        verbose_name = 'Process'
        verbose_name_plural = 'Processes'

    process_type = models.ForeignKey(
        ProcessType,
        on_delete=models.CASCADE,
        related_name='processes',
    )
    phone = models.ForeignKey(
        'phones.Phone',
        on_delete=models.CASCADE,
        related_name='processes',
    )
    status = models.CharField(
        max_length=20,
        choices=ProcessStatus.choices,
        default=ProcessStatus.CREATED,
    )
    notes = models.TextField(
        blank=True,
        default='',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    ended_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.process_type} ({self.status})'

    def save(self, *args, **kwargs):
        if self.status == ProcessStatus.COMPLETED:
            self.ended_at = timezone.now()
        else:
            self.ended_at = None
        super().save()
