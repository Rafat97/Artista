from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class DashboardView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "dashboard_home.html", context)

    def post(self, request, *args, **kwargs):
        pass
