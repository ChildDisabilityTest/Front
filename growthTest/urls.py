from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('userInfo', views.userInfo),
    path('test', views.test),
    path('result', views.result),
    path('bar-chart', views.bar_chart, name='bar-chart'),
] 