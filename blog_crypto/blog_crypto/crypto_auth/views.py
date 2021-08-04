from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from blog_crypto.crypto_auth.forms import SignInForm, SignUpForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/sign_up.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list blogs')
    else:
        form = SignInForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/sign_in.html', context)


def sign_out(request):
    logout(request)
    return redirect('landing')
