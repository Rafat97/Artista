from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse

# from .myform import ClientUserForm
from .forms import ClientUserForm,ArtistUserForm
from pprint import pprint

def register_client(request, *args, **kwargs): 
    if request.session.has_key('user_id'):
        print(request.session['user_id'])
    form = ClientUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() :
            form.save(commit=True)
            response = redirect('register_thank_you')
            return response
        
    context = {
        "form" : form
    }
    return render(request, 'register_client.html', context)


def register_artist(request, *args, **kwargs): 
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

