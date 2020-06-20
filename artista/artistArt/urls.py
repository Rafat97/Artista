from django.urls import path ,include
from .views import ArtistArtUploadNew,ArtistArtPreview

urlpatterns = [
    path('upload/', ArtistArtUploadNew.as_view(), name='artist_art_upload'),
    path('art/<uuid>/', ArtistArtPreview.as_view(), name='artist_art_preview'),
]