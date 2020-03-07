from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs): 
    return render(request, 'landing_page.html', {})