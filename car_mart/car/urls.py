from django.contrib import admin
from django.urls import path
from .views import ListCarCompanies
urlpatterns = [
    path('car-companies/', ListCarCompanies.as_view(), name='car_company_list'),
]
