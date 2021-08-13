from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog_crypto.crypto_blog.models import BlogPost

UserModel = get_user_model()


class CreateBlogPostTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='viktor@abv.bg',
            password='parola123',
        )

    def test_create_blog_post_when_user_logged_in_return_success(self):
        self.client.force_login(self.user)
        data = {
            'title': 'Uppercase letter',
            'content': 'Content.'
        }
        response = self.client.post('/blog/create/', data)
        self.assertEqual(BlogPost.objects.count(), 1)

    def test_create_blog_post_when_there_is_no_user_return_failure(self):
        data = {
            'title': 'Uppercase letter',
            'content': 'Content.',
        }
        response = self.client.post('/blog/create/', data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.count(), 0)

    def test_create_blog_post_when_data_is_not_valid_return_failure(self):
        self.client.force_login(self.user)
        data = {
            'title': 'lowercase letter',
            'content': 'Content.',
        }
        response = self.client.post('/blog/create/', data)
        self.assertEqual(BlogPost.objects.count(), 0)
