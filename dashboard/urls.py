from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('data_to_excel', data_to_excel, name='data_to_excel')
] 