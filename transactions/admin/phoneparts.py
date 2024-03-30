from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter

from transactions.models import PhonePartTransaction


class PhonePartFilter(AutocompleteFilter):
    title = 'Phone Part'
    field_name = 'phone_part'


@admin.register(PhonePartTransaction)
class PhonePartTransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'phone_part',
        'amount',
        'created_at',
    )
    search_fields = (
        'phone_part__name',
        'description',
        'amount',
    )
    raw_id_fields = (
        'phone_part',
    )
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_filter = (
        PhonePartFilter,
    )
