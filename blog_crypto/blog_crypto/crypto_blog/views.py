from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from blog_crypto.crypto_blog.forms import BlogPostForm
from blog_crypto.crypto_blog.models import BlogPost


def list_blogs(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog_list.html', context)


@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('landing')

    else:
        form = BlogPostForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/blog_create.html', context)


def blog_post_details(request, pk):
    blog_post = BlogPost.objects.get(pk=pk)
    is_author = blog_post.author == request.user

    context = {
        'blog': blog_post,
        'is_author': is_author,
    }

    return render(request, 'blog/blog_details.html', context)


def edit_blog_post(request, pk):
    pass
