from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog_crypto.crypto_blog.models import BlogPost, Like

UserModel = get_user_model()


class LikeBlogPostView(TestCase):
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
        self.like_url = reverse('like blog post', args=[self.blog.id])

    def test_like_blog_post_view_when_no_user_logged_in_return_fail(self):
        response = self.client.get(self.like_url)
        self.assertEqual(302, response.status_code)

    def test_like_blog_post_view_user_logged_in_likes_nonexisting_post_return_fail(self):
        self.client.force_login(self.user)
        self.assertEqual(Like.objects.count(), 0)
        with self.assertRaises(Exception) as e:
            response = self.client.post(reverse('like blog post', args=[self.blog.id + 1]))
        self.assertEqual('BlogPost matching query does not exist.', str(e.exception))
        self.assertEqual(Like.objects.count(), 0)

    def test_like_blog_post_view_user_logged_in_likes_existing_post_return_success(self):
        self.client.force_login(self.user)

        self.assertEqual(Like.objects.count(), 0)
        response = self.client.post(self.like_url)
        self.assertEqual(Like.objects.count(), 1)
