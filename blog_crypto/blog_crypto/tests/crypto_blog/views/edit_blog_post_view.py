from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog_crypto.crypto_blog.models import BlogPost

UserModel = get_user_model()


class EditBlogPostView(TestCase):
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
        self.edit_url = reverse('edit', args=[self.blog.id])

    def test_edit_blog_post_view_when_user_not_logged_in_return_fail(self):
        response = self.client.get(self.edit_url)
        self.assertEqual(302, response.status_code)

    def test_edit_blog_post_view_when_user_logged_in_but_data_is_incorrect_return_fail(self):
        self.client.login(
            email='viktor@abv.bg',
            password='parola123',
        )

        response = self.client.get(self.edit_url)
        form = response.context['form']
        data = form.initial
        data['title'] = 'invalid title'
        response = self.client.post(self.edit_url, data)
        blog = BlogPost.objects.get(pk=self.blog.id)
        self.assertEqual(blog.title, 'Valid title')

    def test_edit_blog_post_view_when_user_logged_in_return_success(self):
        self.client.login(
            email='viktor@abv.bg',
            password='parola123',
        )

        response = self.client.get(self.edit_url)
        form = response.context['form']
        data = form.initial
        data['title'] = 'Valid2 title'
        response = self.client.post(self.edit_url, data)
        blog = BlogPost.objects.get(pk=self.blog.id)
        self.assertEqual(blog.title, 'Valid2 title')
