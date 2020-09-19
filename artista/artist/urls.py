from django.urls import path ,include
from .views import DashboardArtistView,SingleArtistView,ArtistReviewView


app_name="artist"
urlpatterns = [
    path('', DashboardArtistView.as_view(), name='home'), #landing page url
    path('features/',include('artistArt.urls')),
    path('artist/<uuid>',SingleArtistView.as_view(), name='single_artist_info'),
    path('review/<uuid>',ArtistReviewView.as_view(), name='artist_review'),
]