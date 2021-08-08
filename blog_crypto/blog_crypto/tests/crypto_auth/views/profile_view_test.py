from django.test import TestCase, Client
from django.urls import reverse

from blog_crypto.crypto_auth.models import CryptoUser, Profile


class SignUpTest(TestCase):
    def test_register_and_profile_success(self):
        client = Client()
        data = {
            'email': 'viktor@abv.bg',
            'password1': '1234',
            'password2': '1234',
        }
        response = client.post(reverse('sign up'), data)
        self.assertEqual(CryptoUser.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)

    def test_register_and_profile_failure(self):
        client = Client()
        data = {
            'email': 'viktorabv.bg',
            'password1': '1234',
            'password2': '1234',
        }
        response = client.post(reverse('sign up'), data)
        self.assertEqual(CryptoUser.objects.count(), 0)
        self.assertEqual(Profile.objects.count(), 0)
        self.assertFalse(response.context['form'].is_valid())