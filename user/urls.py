from django.urls import path
from .views import *

urlpatterns = [
    path('childInfo', childInfo, name="childInfo"),
] 