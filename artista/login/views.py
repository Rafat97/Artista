from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import LoginFrom
from register.models import User

def user_login_redirect(view_func):
    def decorated_view_func(request, *args, **kwargs):
        if request.session.has_key('user'):
            return redirect('/dashboard')
        return view_func(request, *args, **kwargs)
    return decorated_view_func

# @user_login_redirect
def login_user(request, *args, **kwargs):   
    form = LoginFrom(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() :
            user = form.getUser
            request.session['user'] = str(user.uuid)
            return redirect('/dashboard')
           
    context = {
        "form" : form
    }
    return render(request, 'login.html', context)

def logout_user(request, *args, **kwargs): 
    if request.session.has_key('user'):
        del request.session['user']
    response = redirect('home')
    return response


