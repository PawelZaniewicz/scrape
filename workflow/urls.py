from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('workflow/', include('startujemy.urls')),
]

admin.site.site_header = 'Budimex - OUS oraz WMB'