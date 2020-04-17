from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import LoginFrom


def login_user(request, *args, **kwargs): 
    form = LoginFrom(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() :
            user = form.getUser
            request.session['user_id'] = user.id
            pass
    context = {
        "form" : form
    }
    return render(request, 'login.html', context)

