from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter

from transactions.models import UserTransaction


class UserFilter(AutocompleteFilter):
    title = 'User'
    field_name = 'user'


@admin.register(UserTransaction)
class UserTransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'amount',
        'created_at',
    )
    search_fields = (
        'user__username',
        'description',
        'amount',
    )
    raw_id_fields = (
        'user',
    )
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_filter = (
        UserFilter,
    )
