from django.contrib import admin
from .models import ArtCategory,ArtistArt

# Register your models here.
@admin.register(ArtCategory)
class ArtCategory(admin.ModelAdmin):
    pass

@admin.register(ArtistArt)
class ArtistArt(admin.ModelAdmin):
    pass