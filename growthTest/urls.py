from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('result', views.result, name='result'),
    path('bar-chart', views.bar_chart, name='bar-chart'),
] 