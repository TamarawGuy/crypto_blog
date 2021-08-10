from django.test import TestCase, Client
from django.urls import reverse

from blog_crypto.crypto_auth.models import CryptoUser
from blog_crypto.crypto_blog.models import BlogPost


class BlogPostDetailsTest(TestCase):
    def test_blog_post_details(self):
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
        response = client.get(reverse('blog post details', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_details.html')
