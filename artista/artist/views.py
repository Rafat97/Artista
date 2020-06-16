from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from artista.utils import get_current_user

# Create your views here.
class DashboardArtistView(View):
    USER_INFO = None

    def get(self, request, *args, **kwargs):
        self.USER_INFO = get_current_user(request)
        
        if self.USER_INFO == None:
            return redirect('/logout')
        context = {
            'user_info' : self.USER_INFO
        }
        return render(request, "home.html", context)

