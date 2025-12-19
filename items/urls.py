from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.items_list, name='items_list'),
    path('items/<int:id>/', views.item_detail, name='item_detail'),
    path('items/create/', views.create_item, name='create_item'),
    path('items/<int:id>/update/', views.update_item, name='update_item'),
    path('items/<int:id>/update_partial/', views.update_item_partial, name='update_item_partial'),
    path('items/<int:id>/delete/', views.delete_item, name='delete_item'),
    path('items/<int:item_id>/change_status/', views.change_status, name='change_status'),
]
