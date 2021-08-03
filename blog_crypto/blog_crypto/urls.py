from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_crypto.crypto_common.urls')),
    path('auth/', include('blog_crypto.crypto_auth.urls')),
]
