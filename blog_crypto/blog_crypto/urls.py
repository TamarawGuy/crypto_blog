from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('blog_crypto.crypto_common.urls')),
                  path('auth/', include('blog_crypto.crypto_auth.urls')),
                  path('blog/', include('blog_crypto.crypto_blog.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
