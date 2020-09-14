from django.urls import path ,include
from .views import AllArtView,AllArtSearchView


app_name="app_artInfo"
urlpatterns = [
    path('', AllArtView.as_view(), name='home'), #landing page url
    path('search/', AllArtSearchView.as_view(), name='all_art_searching_page'), #Search Url 
]