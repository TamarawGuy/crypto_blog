from django import forms

from blog_crypto.crypto_blog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('author',)


class EditBlogForm(BlogPostForm):
    class Meta:
        model = BlogPost
        exclude = ('author',)
