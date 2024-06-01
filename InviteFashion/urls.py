from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', include('AdminAPI.urls')),
    path('api/', include('InviteFashionAPI.urls')),
    path('admin/', admin.site.urls),
]
