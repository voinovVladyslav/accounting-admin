from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter

from transactions.models import PhoneTransaction


class PhoneFilter(AutocompleteFilter):
    title = 'Phone'
    field_name = 'phone'


@admin.register(PhoneTransaction)
class PhoneTransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'phone',
        'amount',
        'created_at',
    )
    search_fields = (
        'phone__name',
        'description',
        'amount',
    )
    raw_id_fields = (
        'phone',
    )
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_filter = (
        PhoneFilter,
    )
