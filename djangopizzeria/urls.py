from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth-api/', include('rest_framework.urls')),
    # add api
    path('rest-api/v1/', include('djangopizzeria.api')),
]
