from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from artista.utils import get_current_user


class DashboardClientView(View):

    USER_INFO = None

    def get(self, request, *args, **kwargs):
        self.USER_INFO = get_current_user(request)
        
        if self.USER_INFO.user_role.role_name != 'Client':
            return redirect('/dashboard')

        if self.USER_INFO == None:
            return redirect('/logout')

        context = {
            'user_info' : self.USER_INFO
        }
        return render(request, "home.html", context)
