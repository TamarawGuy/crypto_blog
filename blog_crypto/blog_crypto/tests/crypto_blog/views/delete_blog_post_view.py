from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog_crypto.crypto_blog.models import BlogPost

UserModel = get_user_model()


class DeleteBlogPostView(TestCase):
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
        self.delete_url = reverse('delete', args=[self.blog.id])

    def test_delete_blog_post_view_with_user_logged_in_return_success(self):
        self.client.force_login(self.user)
        response = self.client.get(self.delete_url)
        form = response.context['form']
        data = form.initial
        response = self.client.post(self.delete_url, data)
        self.assertEqual(BlogPost.objects.count(), 0)

    def test_delete_blog_post_view_without_user_logged_in_return_fail(self):
        response = self.client.get(self.delete_url)
        self.assertEqual(302, response.status_code)

    def test_delete_blog_post_view_with_nonexisting_blog_post_return_fail(self):
        self.client.force_login(self.user)
        with self.assertRaises(Exception) as e:
            response = self.client.get(reverse('delete', args=[self.blog.id + 1]))
        self.assertEqual('BlogPost matching query does not exist.', str(e.exception))
