from django.contrib import admin
from .models import ArtCategory,ArtistArt

# Register your models here.
@admin.register(ArtCategory)
class ArtCategory(admin.ModelAdmin):
    pass

@admin.register(ArtistArt)
class ArtistArt(admin.ModelAdmin):
    list_display = ('uuid','title','user', 'category', 'created_at','updated_at','id',)
    search_fields = ['title','short_description','long_description']
    pass