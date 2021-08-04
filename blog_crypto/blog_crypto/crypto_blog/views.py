from django.shortcuts import render

from blog_crypto.crypto_blog.models import BlogPost


def list_blogs(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog_list.html', context)


def create_blog_post(request):
    pass


def blog_post_details(request, pk):
    pass


def edit_blog_post(request, pk):
    pass
