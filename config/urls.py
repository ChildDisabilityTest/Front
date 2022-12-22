from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('growthTest.urls')),
    path('user/', include('user.urls')),
    path('dashboard/', include('dashboard.urls')),
]
