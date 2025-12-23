from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # Columns to show in the list view
    list_display = ['id', 'item_code', 'name', 'quantity', 'reorder_level', 'status', 'created_at', 'updated_at']

    # Filters on the right sidebar
    list_filter = ['status', 'created_at']

    # Search box
    search_fields = ['name', 'item_code']

    # Default ordering
    ordering = ['name']
