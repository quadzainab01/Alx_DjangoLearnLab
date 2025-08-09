from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),  # 🔥 Make sure your app URLs are included here
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
