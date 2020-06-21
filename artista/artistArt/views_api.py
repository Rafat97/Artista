from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ArtistArt,ArtCategory,ArtComment,ArtLikeDislike
from register.models import User
from artista.utils import get_current_user
from rest_framework import serializers,viewsets
from django.core import serializers as django_core_serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import filters
from django.http import JsonResponse
import json

class ArtistArtCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtCategory
        fields = '__all__'

class ArtistArtUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['display_name','id','uuid','avatar',]

class ArtistArtSerializer(serializers.ModelSerializer):
    category = ArtistArtCategorySerializer(many=False, read_only=True)
    user = ArtistArtUserSerializer(many=False, read_only=True)
    current_custom_user_liked = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ArtistArt
        fields = [
            'id',
            'title',
            'uuid',
            'short_description',
            'long_description',
            'view_count',
            'post_status',
            'number_of_likes',
            'number_of_dislikes',
            'current_custom_user_liked',
            'image',
            'user',
            'category',
            'created_at'
        ]
    
    def get_current_custom_user_liked(self, obj):
        '''
        response  
        null : current user have no data like & no dislike 
        true : current user liked this post
        false : current user disliked this post
        '''
        is_liked = None
        request = self.context.get('request')
        current_user = get_current_user(request)
        if current_user:
            data =  obj.current_user_like_dislike(current_user)
            if data:
                is_liked = data.get().like_dislike  

        return is_liked



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


class ArtistArtApi_all(generics.ListAPIView):
    queryset = ArtistArt.objects.all()
    serializer_class = ArtistArtSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'tags',]
    ordering_fields = ['view_count',]
    filterset_fields = ['post_status',]

    # def get_serializer_context(self):
    #     return  {
    #         'request': self.request,
    #     }
    
    # def get(self, request, *args, **kwargs):
    #     return self.list(request)

    # Not used post request
    # def post(self, request, *args, **kwargs):
    #     return self.list(request)

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
