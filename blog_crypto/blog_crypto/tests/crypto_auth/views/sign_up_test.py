from django.test import TestCase
from django.urls import reverse

from blog_crypto.crypto_auth.models import CryptoUser, Profile


class SignUpTest(TestCase):
    def setUp(self):
        self.incorrect_data = {
            'email': 'viktorabv.bg',
            'password1': 'Mnogoslojnaparola123*',
            'password2': 'Mnogoslojnaparola123*',
        }

    def test_sign_up_view_get(self):
        response = self.client.get(reverse('sign up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/sign_up.html')

    def test_sign_up_view_post_success(self):
        response = self.client.get(reverse('sign up'))
        form = response.context['form']
        data = form.initial
        data['email'] = 'viktor@abv.bg'
        data['password1'] = 'Mnogoslojnaparola123*'
        data['password2'] = 'Mnogoslojnaparola123*'
        response = self.client.post(reverse('sign up'), data)
        c = CryptoUser.objects.count()
        p = Profile.objects.count()
        self.assertEqual(CryptoUser.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)

    def test_sign_up_view_post_failure(self):
        response = self.client.post(reverse('sign up'), self.incorrect_data)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertEqual(CryptoUser.objects.count(), 0)
        self.assertEqual(Profile.objects.count(), 0)
