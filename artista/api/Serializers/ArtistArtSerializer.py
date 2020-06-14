from rest_framework import serializers
from register.models import User
from artistArt.models import ArtCategory,ArtistArt

# Serializers define the API representation.
class ArtistArtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArtistArt
        fields = '__all__'

class ArtCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArtCategory
        fields = '__all__'