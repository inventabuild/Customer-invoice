from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('item_new/', views.item_new, name = 'item_new'),
    path('item_view/<int:id>/', views.item_view, name = 'item_view'),
    path('item_list/', views.item_list, name = 'item_list')
]