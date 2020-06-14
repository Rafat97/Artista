from rest_framework import serializers,viewsets,routers
from register.models import User
from artistArt.models import ArtCategory,ArtistArt
from ..Serializers.ArtistArtSerializer import ArtistArtSerializer,ArtCategorySerializer

# ViewSets define the view behavior.
class ArtistArtViewSet(viewsets.ModelViewSet):
    queryset = ArtistArt.objects.all()
    serializer_class = ArtistArtSerializer

# ViewSets define the view behavior.
class ArtCategoryViewSet(viewsets.ModelViewSet):
    queryset = ArtCategory.objects.all()
    serializer_class = ArtCategorySerializer