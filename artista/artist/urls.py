from django.urls import path ,include
from .views import DashboardArtistView


# app_name="artist"
urlpatterns = [
    path('', DashboardArtistView.as_view(), name='home'), #landing page url
    path('features/',include('artistArt.urls')),
]