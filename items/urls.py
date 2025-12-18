from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.items_list, name='items_list'),
    path('items/<int:id>/', views.item_detail, name='item_detail'),
    path('items/<int:id>/update/', views.update_item, name='update_item'),
    path('items/<int:id>/delete/', views.delete_item, name='delete_item'),
]
