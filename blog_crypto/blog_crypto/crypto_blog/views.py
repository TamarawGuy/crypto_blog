from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from blog_crypto.crypto_blog.forms import BlogPostForm, EditBlogForm, DeleteBlogForm
from blog_crypto.crypto_blog.models import BlogPost, Like


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
    is_liked = blog_post.like_set.filter(user_id=request.user.id).first()
    likes = blog_post.like_set.count()
    context = {
        'blog': blog_post,
        'is_author': is_author,
        'is_liked': is_liked,
        'likes': likes,
    }

    return render(request, 'blog/blog_details.html', context)


@login_required
def edit_blog_post(request, pk):
    blog = BlogPost.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditBlogForm(instance=blog)

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, 'blog/blog_edit.html', context)


def delete_blog(request, pk):
    blog = BlogPost.objects.get(pk=pk)
    form = DeleteBlogForm(instance=blog)
    if request.method == 'POST':
        blog.delete()
        return redirect('profile details')

    context = {
        'blog': blog,
        'form': form,
    }

    return render(request, 'blog/blog_delete.html', context)


@login_required
def like_blog_post(request, pk):
    blog_post = BlogPost.objects.get(pk=pk)
    liked_by_user = blog_post.like_set.filter(user_id=request.user.id).first()

    if liked_by_user:
        liked_by_user.delete()
    else:
        like = Like(
            blog=blog_post,
            user=request.user,
        )
        like.save()
    return redirect('blog post details', blog_post.id)
