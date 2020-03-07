from django.http import HttpResponse
from django.shortcuts import render


def login(request, *args, **kwargs): 
    return render(request, 'login.html', {})