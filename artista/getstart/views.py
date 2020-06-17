from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from htmlmin.decorators import minified_response

# class base view
class HomePageView(View):
    @minified_response
    def get(self, request, *args, **kwargs):
        request.session['app_name'] = "Artista"
        # del request.session['app_name']
        return render(request, 'landing_page.html', {})

# function base view
@minified_response
def home_view(request, *args, **kwargs): 
    return render(request, 'landing_page.html', {})