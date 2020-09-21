from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from register.models import User

# Create your views here.


class DashboardView(View):
    """
    Display an Artist Account

    **Context**

    ``mymodel``
        An instance of :model:`myapp.User`.

    **Redrict:**

    :Redrict Url name:/dashboard/art base on Artist or Client
    """

    def get(self, request, *args, **kwargs):

        if not request.session.has_key('user'):
            return redirect('/')

        uuid = request.session['user']
        user = User.objects.filter(uuid__exact=uuid).get()
        if user.user_role.role_name == 'Client':
            return redirect('/dashboard/art')

        elif user.user_role.role_name == 'Artist':
            return redirect('/dashboard/art')

        else:
            return redirect('/')
        # context = {}
        # return render(request, "dashboard_home.html", context)

    def post(self, request, *args, **kwargs):
        pass
