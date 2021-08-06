from django.urls import path

from blog_crypto.crypto_auth.views import sign_up, sign_in, sign_out, profile_details

urlpatterns = (
    path('sign-up/', sign_up, name='sign up'),
    path('sign-in/', sign_in, name='sign in'),
    path('sign-out/', sign_out, name='sign out'),
    path('profile/', profile_details, name='profile details'),
)