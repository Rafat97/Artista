from django.contrib import admin
from django.urls import path ,include
from django.conf.urls import url
from rest_framework import serializers,viewsets,routers

from .ViewSets.UserViewSet import UserViewSet
from .ViewSets.ArtistArtViewSet import ArtistArtViewSet,ArtCategoryViewSet


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'artist_art', ArtistArtViewSet)
router.register(r'art_category', ArtCategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls'))
]
