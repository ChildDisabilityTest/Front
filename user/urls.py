from django.urls import path
from .views import *

urlpatterns = [
    path('userInfo', userInfo, name="userInfo"),
] 