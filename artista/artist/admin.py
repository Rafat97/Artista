from django.contrib import admin
from .models import ArtistReview
# Register your models here.
# Register your models here.
@admin.register(ArtistReview)
class ArtistReview(admin.ModelAdmin):
    list_display = ('message','user_reviewing', 'user_reviewer', 'created_at','updated_at','id',)
    pass