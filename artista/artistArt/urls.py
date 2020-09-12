from django.urls import path ,include
from .views import ArtistArtUploadNew,ArtistArtPreview,ArtistArtUploadEdit,ArtistArtPreviewAll,ArtistArtUploadedDelete

urlpatterns = [
    path('upload/', ArtistArtUploadNew.as_view(), name='artist_art_upload'),
    path('upload/<uuid>/edit', ArtistArtUploadEdit.as_view(), name='artist_art_upload_edit'),
    path('upload/<uuid>/delete', ArtistArtUploadedDelete.as_view(), name='artist_art_uploaded_delete'),
    path('art_all/', ArtistArtPreviewAll.as_view(), name='artist_own_all_art'),
    path('art/<uuid>/', ArtistArtPreview.as_view(), name='artist_art_preview'),
]