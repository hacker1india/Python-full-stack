

from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    # Web Views
    path('', views.index, name='index'),
    path('items/', views.item_list, name='item_list'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/update/<int:pk>/', views.update_item, name='update_item'),
    path('items/delete/<int:pk>/', views.delete_item, name='delete_item'),

    # API Views
    path('api/items/', api_views.ItemListCreateAPIView.as_view(), name='api_item_list_create'),
    path('api/items/<int:pk>/', api_views.ItemRetrieveUpdateDestroyAPIView.as_view(), name='api_item_detail'),
]
