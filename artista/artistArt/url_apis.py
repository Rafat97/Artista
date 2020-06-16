from django.urls import path ,include
from .views_api import ArtistArtApi_all,ArtistArtApi_single

urlpatterns = [
    path('art/', ArtistArtApi_all.as_view(), name='artist_art_api_all_get'),
    path('art/<int:pk>/', ArtistArtApi_single.as_view(), name='artist_single_art_api_get'),
]