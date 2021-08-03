from django.urls import path

from blog_crypto.crypto_common.views import landing_page

urlpatterns = (
    path('', landing_page, name='landing'),
)