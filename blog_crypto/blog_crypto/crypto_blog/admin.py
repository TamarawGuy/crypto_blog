from django.contrib import admin

from blog_crypto.crypto_blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass