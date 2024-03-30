from django.contrib import admin


from .models import Process, ProcessType


@admin.register(ProcessType)
class ProcessTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )
    search_fields = (
        'name',
        'description',
    )


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'process_type',
        'phone',
        'status',
        'created_at',
        'updated_at',
        'ended_at',
    )
    search_fields = (
        'process_type__name',
        'phone__name',
        'status',
    )
    raw_id_fields = (
        'process_type',
        'phone',
    )
    list_filter = (
        'status',
        'process_type',
    )
