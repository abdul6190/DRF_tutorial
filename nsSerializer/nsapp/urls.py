from django.urls import path
from .views import CustomerList, CustomerDetails, OrderList, OrderDetails

urlpatterns = [
    path('customer', CustomerList.as_view()),
    path('customer/<int:pk>', CustomerDetails.as_view()),
    path('orders', OrderList.as_view()),
    path('orders/<int:pk>', OrderDetails.as_view()),
]
