from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class DashboardClientView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("asdasd")
