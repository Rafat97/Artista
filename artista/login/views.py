from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import LoginFrom
from register.models import User

def login_user(request, *args, **kwargs): 
    form = LoginFrom(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() :
            user = form.getUser
            request.session['user'] = str(user.uuid)
            # print(User.objects.get(uuid__exact=(str(user.uuid))))

    context = {
        "form" : form
    }
    return render(request, 'login.html', context)

