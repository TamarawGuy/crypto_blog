from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from django.urls import reverse

from blog_crypto.crypto_auth.models import CryptoUser

UserModel = get_user_model()


class SignInTest(TestCase):
    def setUp(self):
        self.data = {
            'email': 'viktor@abv.bg',
            'password': 'Mnogoslojnaparola123*',
        }
        self.invalid_data = {
            'email': 'viktor@abv.bg',
            'password': 'Mnogoslojnaparola123**',
        }

    def test_sign_in_view_get(self):
        response = self.client.get(reverse('sign in'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/sign_in.html')

    def test_sign_in_when_password_is_invalid(self):
        pass

    def test_sign_in_when_user_created_return_success(self):
        self.user = UserModel.objects.create_user(
            email='viktor@abv.bg',
            password='Mnogoslojnaparola123*',
        )

        response = self.client.post(reverse('sign in'), self.data)
        response = self.client.get(reverse('profile details'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/profile.html')
