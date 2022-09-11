from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customer_new/', views.customer_new, name='customer_new' ),
    path('customer_view/<int:id>', views.customer_view, name='customer_view'),
    path('customer_list/', views.customer_list, name='customer_list'),
]
