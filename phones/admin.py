from django.contrib import admin

from phones.models import Phone


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
