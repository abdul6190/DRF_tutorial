from django.urls import path
from .views import passenger_list, passenger_details

urlpatterns = [
    path('', passenger_list, name="passenger_list"),
    path('<int:id>/', passenger_details, name="passenger_details"),
]