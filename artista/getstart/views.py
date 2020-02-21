from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs): 
    text = """<h1> ARTISTA! </h1>"""
    return HttpResponse(text)
