"""artista URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include

from getstart.views import home_view
from login.views import login
from register.views import register_client,register_artist

urlpatterns = [
    path('', home_view, name='home'), #landing page url
    path('api/',include('api.urls')), #api page url

    path('register/artist/', register_artist,name='register_artist'), #artist register page url
    path('register/client/', register_client,name='register_client'), #client register page url
    
    # path('login/', login),  #login page url

    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    
]
