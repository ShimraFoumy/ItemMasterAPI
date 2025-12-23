from django.urls import path
from .views import (
    ItemListView,
    item_detail,
    create_item,
    update_item,
    update_item_partial,
    delete_item,
    change_status
)

urlpatterns = [
    # List all items (with pagination, sorting, filtering)
    path('items/', ItemListView.as_view(), name='items_list'),

    # CRUD endpoints
    path('items/<int:id>/', item_detail, name='item_detail'),
    path('items/create/', create_item, name='create_item'),
    path('items/<int:id>/update/', update_item, name='update_item'),
    path('items/<int:id>/partial/', update_item_partial, name='update_item_partial'),
    path('items/<int:id>/delete/', delete_item, name='delete_item'),
    path('items/<int:item_id>/status/', change_status, name='change_status'),
]
