from django.views import debug
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('default-welcome-page/', debug.default_urlconf),
    path('admin/', admin.site.urls),
    path('reverse/', include('reverse.urls')),
    path('guess/', include('guess.urls')),
]
