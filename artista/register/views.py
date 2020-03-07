from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

def register_client(request, *args, **kwargs): 
    form = ClientUserForm(request.POST or None)
    if request.POST:
        if form.is_valid() :
            print(form.cleaned_data)
        # else:
        #     print( user_form.errors )
        # pass
    
    context = {
        "form" : form
    }
    return render(request, 'register_client.html', context)
