from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name='customer_pricing_new'),
    path('view/<int:id>', views.view, name='customer_pricing_view'),
    path('list/', views.list, name='customer_pricing_list'),
]