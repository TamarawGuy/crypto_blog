from django.test import TestCase, Client
from unittest.mock import patch

import blog_crypto.crypto_auth.signals
from blog_crypto.crypto_auth.forms import SignUpForm
from blog_crypto.crypto_auth.models import Profile


class UserCreatedTest(TestCase):
    def test_user_created_signal_creates_profile_when_success(self):
        form = SignUpForm()
        form.cleaned_data = {
            'email': 'viktor@abv.bg',
            'password1': 'parola123',
            'password2': 'parola123',
        }
        form.save()
        profile_count = Profile.objects.count()
        self.assertEqual(profile_count, 1)
