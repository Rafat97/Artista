from django.http import HttpResponse
from django.shortcuts import render
# from .myform import ClientUserForm
from .forms import ClientUserForm,ArtistUserForm
from pprint import pprint

def register_client(request, *args, **kwargs): 
    if request.session.has_key('user_id'):
        print(request.session['user_id'])
    form = ClientUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() :
            print(form.cleaned_data)
            save = form.save()
            request.session['user_id'] = save.id
        else:
            print( form.errors )

    context = {
        "form" : form
    }
    return render(request, 'register_client.html', context)


def register_artist(request, *args, **kwargs): 
    
    form = ArtistUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() :
            print(form.cleaned_data)
            form.save()
        else:
            print( form.errors )

    context = {
        "form" : form
    }
    return render(request, 'register_artist.html', context)
