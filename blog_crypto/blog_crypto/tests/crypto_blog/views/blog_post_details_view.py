from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog_crypto.crypto_blog.models import BlogPost

UserModel = get_user_model()


class BlogPostDetailsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='viktor@abv.bg',
            password='parola123',
        )
        self.blog = BlogPost.objects.create(
            title='Valid title',
            content='Valid content.',
            author_id=self.user.id,
        )

    def test_blog_post_details_with_user_logged_in_return_success(self):
        self.client.force_login(self.user)

        self.assertEqual(BlogPost.objects.count(), 1)
        response = self.client.get(reverse('blog post details', args=[self.blog.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_details.html')

    def test_blog_post_details_without_user_logged_in_return_success(self):
        self.assertEqual(BlogPost.objects.count(), 1)
        response = self.client.get(reverse('blog post details', args=[self.blog.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_details.html')

    def test_blog_post_details_view_when_no_such_post_is_created_return_fail(self):
        with self.assertRaises(Exception) as e:
            response = self.client.get(reverse('blog post details', args=[self.blog.id + 1]))
        self.assertEqual('BlogPost matching query does not exist.', str(e.exception))
