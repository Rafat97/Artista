from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ArtistArt,ArtCategory
from register.models import User
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import mixins

class ArtistArtCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtCategory
        fields = '__all__'

class ArtistArtUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['display_name','id','uuid','avatar',]

class ArtistArtSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False)
    category = ArtistArtCategorySerializer(many=False, read_only=True)
    user = ArtistArtUserSerializer(many=False, read_only=True)
    class Meta:
        model = ArtistArt
        fields = ['id','title','uuid','short_description','long_description','post_status','image','user','category','created_at']
        


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'meta' : {
                'current_page': self.page.number,
                'total_count': self.page.paginator.count,
                'per_page': self.page_size,
            },
            'data': data
        })


class ArtistArtApi_all(generics.GenericAPIView
                        ,mixins.ListModelMixin
                        ,mixins.CreateModelMixin
                        ):
    queryset = ArtistArt.objects.all()
    serializer_class = ArtistArtSerializer
    pagination_class = StandardResultsSetPagination
    class Meta:
        ordering = ['-id']

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.list(request)

class ArtistArtApi_single(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtistArt.objects.all()
    serializer_class = ArtistArtSerializer

# because for REST_FRAMEWORK default setting `DEFAULT_PERMISSION_CLASSES`
# @permission_classes((permissions.AllowAny,))
# class ArtistArtApi(APIView):
#     pagination_class = StandardResultsSetPagination

#     def get(self, request, format=None):
        
#         artist_art = ArtistArt.objects.all()
#         serializer = ArtistArtSerializer(artist_art, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
