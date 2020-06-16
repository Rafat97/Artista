from django.urls import path ,include
from .views import ArtistArtUploadNew

urlpatterns = [
    path('upload/', ArtistArtUploadNew.as_view(), name='artist_art_upload'),
]