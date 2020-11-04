from django.views import debug
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('default-welcome-page/', debug.default_urlconf),
    path('admin/', admin.site.urls),
]
