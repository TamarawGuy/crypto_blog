from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path

from blog_crypto.crypto_auth.views import sign_up, sign_in, sign_out, profile_details

urlpatterns = (
    path('sign-up/', sign_up, name='sign up'),
    path('sign-in/', sign_in, name='sign in'),
    path('sign-out/', sign_out, name='sign out'),
    path('profile/', profile_details, name='profile details'),

    path('password-reset/',
         PasswordResetView.as_view(
             template_name='auth/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='auth/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='auth/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(
             template_name='auth/password_reset_complete.html'
         ),
         name='password_reset_complete'),
)
