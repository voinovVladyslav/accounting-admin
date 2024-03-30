from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter

from phones.models import Phone, PhonePart


class PhoneFilter(AutocompleteFilter):
    title = 'Phone'
    field_name = 'phone'
    order_by = ('name',)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'imei',
        'name',
        'estimated_price',
        'status',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'name',
        'imei',
    )


@admin.register(PhonePart)
class PhonePartAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
    )
    search_fields = (
        'name',
        'phone__name',
    )
    list_filter = (
        PhoneFilter,
    )
