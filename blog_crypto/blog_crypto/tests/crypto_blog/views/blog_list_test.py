from django.test import TestCase, Client
from django.urls import reverse


class BlogListTest(TestCase):
    def test_blog_list_page(self):
        client = Client()
        response = client.get(reverse('list blogs'))
        blog_posts = response.context['blogs']
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')
