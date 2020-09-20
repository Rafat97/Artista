from django.urls import path, include
from . import views
from .views import ArtistFollowView, ArtistFollowViewFormSubmit

urlpatterns = [
    path('now_following', ArtistFollowView.as_view(), name='artist_follow'),
    path('new_following/<uuid>', ArtistFollowViewFormSubmit.as_view(),
         name='artist_follow_form_submit'),
    #path('following', views.following, name='following'),
]
