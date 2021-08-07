from django.urls import path

from blog_crypto.crypto_blog.views import create_blog_post, edit_blog_post, blog_post_details, list_blogs, \
    like_blog_post

urlpatterns = (
    path('blogs/', list_blogs, name='list blogs'),
    path('create/', create_blog_post, name='create'),
    path('edit/<int:pk>', edit_blog_post, name='edit'),
    path('details/<int:pk>', blog_post_details, name='blog post details'),
    path('like/<int:pk>', like_blog_post, name='like blog post'),
)
