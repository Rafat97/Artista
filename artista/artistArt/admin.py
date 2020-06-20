from django.contrib import admin
from .models import ArtCategory,ArtistArt,ArtLikeDislike,ArtComment

# Register your models here.
@admin.register(ArtCategory)
class ArtCategory(admin.ModelAdmin):
    pass

@admin.register(ArtistArt)
class ArtistArt(admin.ModelAdmin):
    list_display = ('uuid','title','user', 'view_count', 'category', 'created_at','updated_at','id',)
    search_fields = ['title','short_description','long_description']
    pass

@admin.register(ArtLikeDislike)
class ArtLikeDislike(admin.ModelAdmin):
    list_display = ('user', 'artist_art', 'like_dislike', 'created_at', 'updated_at', 'id',)
    pass

@admin.register(ArtComment)
class ArtComment(admin.ModelAdmin):
    # list_display = ('uuid','title','user', 'view_count', 'category', 'created_at','updated_at','id',)
    # search_fields = ['title','short_description','long_description']
    pass