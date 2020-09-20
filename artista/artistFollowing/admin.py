from django.contrib import admin
from .models import ArtistFollow

# Register your models here.


@admin.register(ArtistFollow)
class ArtistReview(admin.ModelAdmin):
    list_display = ('user_following', 'user_follower',
                    'created_at', 'updated_at', 'id',)
    pass
