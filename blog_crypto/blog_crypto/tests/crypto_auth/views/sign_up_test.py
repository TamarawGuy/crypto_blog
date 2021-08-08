from django.test import TestCase, Client
from django.urls import reverse

from blog_crypto.crypto_auth.models import CryptoUser, Profile


class SignUpTest(TestCase):
    def test_register_view_get(self):
        client = Client()
        response = client.get(reverse('sign up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/sign_up.html')

    def test_register_view_post_success(self):
        client = Client()
        data = {
            'email': 'viktor@abv.bg',
            'password1': '1234',
            'password2': '1234',
        }
        response = client.post(reverse('sign up'), data)
        self.assertEqual(CryptoUser.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)

    def test_register_view_post_failure(self):
        client = Client()
        data = {
            'email': 'viktorabv.bg',
            'password1': '1234',
            'password2': '1234',
        }
        response = client.post(reverse('sign up'), data)
        self.assertFalse(response.context['form'].is_valid())