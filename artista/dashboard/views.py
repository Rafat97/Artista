from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from register.models import User

# Create your views here.
class DashboardView(View):
    def get(self, request, *args, **kwargs):
        if not request.session.has_key('user'):
            return redirect('/')

        uuid = request.session['user']
        user = User.objects.filter(uuid__exact=uuid).get()
        if user.user_role == 'client':
            return redirect('/dashboard/client')
            
        elif user.user_role == 'artist':
            return redirect('/dashboard/artist')
            
        else:
            return redirect('/')
        # context = {}
        # return render(request, "dashboard_home.html", context)

    def post(self, request, *args, **kwargs):
        pass
