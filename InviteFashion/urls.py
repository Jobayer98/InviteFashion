from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/admin/', include('AdminAPI.urls')),
    path('api/v1/', include('InviteFashionAPI.urls')),
    path('admin/', admin.site.urls),
]
