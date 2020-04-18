from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# class base view
class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing_page.html', {})

# function base view
def home_view(request, *args, **kwargs): 
    return render(request, 'landing_page.html', {})