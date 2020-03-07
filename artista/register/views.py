from django.http import HttpResponse
from django.shortcuts import render


def register_client(request, *args, **kwargs): 
    return render(request, 'register_client.html', {})