from django.test import TestCase, Client
from django.urls import reverse

from blog_crypto.crypto_auth.models import CryptoUser, Profile


class ProfileViewTest(TestCase):
    def test_profile_view_create_user_and_access_profile_page_return_success(self):
        data_sign_up = {
            'email': 'viktor@abv.bg',
            'password1': 'Mnogoslojnaparola123*',
            'password2': 'Mnogoslojnaparola123*',
        }

        data_sign_in = {
            'email': 'viktor@abv.bg',
            'password': 'Mnogoslojnaparola123*',
        }
        response = self.client.post(reverse('sign up'), data_sign_up)
        response = self.client.post(reverse('sign in'), data_sign_in)
        self.assertEqual(CryptoUser.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)
        response = self.client.get(reverse('profile details'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/profile.html')
