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

from getstart.views import home_view,HomePageView
from register.views import register_client,register_artist,thank_you
from login.views import login_user,logout_user
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "ARTISTA Admin"
admin.site.site_title = "ARTISTA Admin Portal"
admin.site.index_title = "Welcome to ARTISTA Portal"

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), #landing page url
    path('api/',include('api.urls')), #api page url

    path('login/', login_user,name='login_user'), #artist login page url app (login)
    path('logout/', logout_user,name='logout_user'), #artist login page url app (login)

    path('register/artist/', register_artist,name='register_artist'), #artist register page url  app (register)
    path('register/client/', register_client,name='register_client'), #client register page url app (register)
    path('register/thankyou/',thank_you ,name='register_thank_you'), #artist register page url app (register)
    

    path('dashboard/', include('dashboard.urls')),
    path('dashboard/artist', include('artist.urls')),
    path('dashboard/client', include('client.urls')),
   
    path('chat/', include('chat.urls')), # must need asynchronous server 
    
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)