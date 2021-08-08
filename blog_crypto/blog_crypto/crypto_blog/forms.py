from django import forms
from django.core.exceptions import ValidationError

from blog_crypto.crypto_blog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('author',)

    def clean_title(self):
        title = self.cleaned_data['title']

        if not title[0].isupper():
            raise ValidationError('Title must start with capital letter.')

        if title.endswith('.'):
            raise ValidationError("Title must not end with '.'")

        return title

    def clean_content(self):
        content = self.cleaned_data['content']

        if not content[0].isupper():
            raise ValidationError('Content must start with capital letter.')

        if not content.endswith('.') or content.endswith('!') or content.endswith('?'):
            raise ValidationError("Content must end with one of these symbols: '.', '!', '?'")

        return content


class EditBlogForm(BlogPostForm):
    class Meta:
        model = BlogPost
        exclude = ('author',)
