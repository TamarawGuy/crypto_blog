from django.test import TestCase

from blog_crypto.crypto_blog.forms import BlogPostForm


class BlogFormTest(TestCase):
    def test_title_starting_with_lowercase_return_exception(self):
        form_data = {
            'title': 'lowercase letter',
            'content': 'Content.'
        }
        form = BlogPostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_title_starting_with_uppercase_return_success(self):
        form_data = {
            'title': 'Uppercase title',
            'content': 'Content.',
        }
        form = BlogPostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_content_starting_with_lowercase_return_exception(self):
        form_data = {
            'title': 'Uppercase letter',
            'content': 'content.',
        }
        form = BlogPostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_content_ending_with_letter_return_exception(self):
        form_data = {
            'title': 'Uppercase letter',
            'content': 'Content',
        }
        form = BlogPostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_content_starting_with_uppercase_and_ending_with_ending_symbol_return_success(self):
        form_data = {
            'title': 'Uppercase title',
            'content': 'Content.',
        }
        form = BlogPostForm(data=form_data)
        self.assertTrue(form.is_valid())
