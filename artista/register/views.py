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
    Display an Client Account

    **Context**

    ``mymodel``
        An instance of :model:`myapp.User`.

    **Template:**

    :template:`register_client.html`
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
    Display an Artist Account

    **Context**

    ``mymodel``
        An instance of :model:`myapp.User`.

    **Template:**

    :template:`register_artist.html`
    """
    form = ArtistUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() :
            form.save(commit=True)
            response = redirect('register_thank_you')
            return response
        
    context = {
        "form" : form
    }
    return render(request, 'register_artist.html', context)


def thank_you(request, *args, **kwargs): 
    print(kwargs)
    context = {}
    return render(request, 'thank_you.html', context)

