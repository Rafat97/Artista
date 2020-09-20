from django.urls import path ,include
from .views import AllArtView,AllArtSearchView,SingleArtView,SingleArtComment,ArtistArtReact,ArtistArtReactAllArt


app_name="app_artInfo"
urlpatterns = [
    path('', AllArtView.as_view(), name='home'), #landing page url
    path('single/<uuid>/', SingleArtView.as_view(), name='artist_single_art_page'), #landing page url
    path('search/', AllArtSearchView.as_view(), name='all_art_searching_page'), #Search Url 
    path('comment/<image_uuid>/<type>', SingleArtComment.as_view(), name='artist_single_art_comment'), #Search Url 
    path('react/<uuid>/', ArtistArtReact.as_view(), name='artist_art_react'),
    path('my_loved_art/', ArtistArtReactAllArt.as_view(), name='artist_reacted_all_art'), 
]