from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

# from .myform import ClientUserForm
from .forms import ClientUserForm, ArtistUserForm
from pprint import pprint


def user_login_redirect(view_func):
    def decorated_view_func(request, *args, **kwargs):
        if request.session.has_key('user'):
            return redirect('/dashboard')
        return view_func(request, *args, **kwargs)
    return decorated_view_func

# @user_login_redirect


def register_client(request, *args, **kwargs):
    """
    reagister User as a client

    **Super Class**

        from django.views import View

    **Method User:**

       GET,POST

    **Context**

        getUser: register.form.ClientUserForm.\n

    **Template:**

        View Templates directory: register/templates/register_client.html
        View redirect ur name : register_thank_you
    """
    if request.session.has_key('user_id'):
        print(request.session['user_id'])
    form = ClientUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            response = redirect('register_thank_you')
            return response

    context = {
        "form": form
    }
    return render(request, 'register_client.html', context)

# @user_login_redirect


def register_artist(request, *args, **kwargs):
    """
    reagister User as a Artist

    **Super Class**

        from django.views import View

    **Method User:**

       GET,POST

    **Context**

        getUser: register.form.ArtistUserForm.\n

    **Template:**

        View Templates directory: register/templates/register_client.html
        View redirect ur name : register_artist
    """
    form = ArtistUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            response = redirect('register_thank_you')
            return response

    context = {
        "form": form
    }
    return render(request, 'register_artist.html', context)


def thank_you(request, *args, **kwargs):
    """
    After login & register thank you page

    **Super Class**

        from django.views import View

    **Method User:**

       GET,POST

    **Template:**

        View Templates directory: register/templates/thank_you.html
    """
    print(kwargs)
    context = {}
    return render(request, 'thank_you.html', context)
