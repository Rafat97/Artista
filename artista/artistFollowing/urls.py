from django.urls import path, include
from . import views
from .views import ArtistFollow

urlpatterns = [
    path('now_following', ArtistFollow.as_view(), name='artist_follow'),
    #path('following', views.following, name='following'),
]
