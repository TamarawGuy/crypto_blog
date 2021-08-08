from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from django.urls import reverse

from blog_crypto.crypto_auth.models import CryptoUser
from blog_crypto.crypto_blog.forms import BlogPostForm
from blog_crypto.crypto_blog.models import BlogPost


class CreateBlogPostTest(TestCase):
    def test_create_blog_post_success(self):
        client = Client()
        data_user = {
            'email': 'viktor@abv.bg',
            'password': '1234',
        }
        CryptoUser.objects.create_user(**data_user)

        response = client.post('/auth/sign-in/', data_user, follow=True)
        data = {
            'title': 'Uppercase letter',
            'content': 'Content.'
        }
        response = client.post('/blog/create/', data)
        self.assertEqual(BlogPost.objects.count(), 1)

    def test_create_blog_post_failure(self):
        client = Client()
        data_user = {
            'email': 'viktor@abv.bg',
            'password': '1234',
        }
        user = CryptoUser.objects.create_user(**data_user)
        response = client.post('/auth/sign-in/', data_user, follow=True)
        data = {
            'title': 'lowercase letter',
            'content': 'Content.',
        }
        response = client.post('/blog/create/', data)
        self.assertEqual(BlogPost.objects.count(), 0)