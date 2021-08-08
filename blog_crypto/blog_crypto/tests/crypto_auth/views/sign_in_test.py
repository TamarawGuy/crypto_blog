from django.test import TestCase, Client

from blog_crypto.crypto_auth.models import CryptoUser


class SignInTest(TestCase):
    def test_login(self):
        client = Client()
        data = {
            'email': 'viktor@abv.bg',
            'password': '1234',
        }
        CryptoUser.objects.create_user(**data)

        response = client.post('/auth/sign-in/', data, follow=True)
        self.assertFalse(response.context['user'].is_superuser)
