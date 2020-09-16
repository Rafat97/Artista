from django.db import models
import uuid
from datetime import datetime
from register.models import User
from artista.utils import get_current_user
import os
import uuid

# Create your models here.
class ArtCategory(models.Model):
   category_name=models.CharField(max_length=100,blank=False)

   def __str__(self):
        return self.category_name

def art_directory_stor_path(instance, filename):
    name, extension = os.path.splitext(filename)
    myDate = datetime.now()
    currentFilename = str(uuid.uuid4().hex)+ extension
    formatedDate = myDate.strftime("%Y-%m-%d")
    path = 'art_image/{0}/{1}'.format(formatedDate, currentFilename)
    return path

class ArtistArt(models.Model):
    STATUS = (
        ('public', 'Public'),
        ('draft', 'Draft'),
        ('private', 'Private')
    )
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    title=models.CharField(max_length=100,blank=False)
    short_description=models.CharField(max_length=300,blank=False)
    long_description=models.CharField(max_length=500,blank=False)
    tags=models.CharField(max_length=1000,blank=True)
    view_count=models.BigIntegerField(default=0)
    post_status = models.CharField(max_length=20,null=False,choices=STATUS,default='private')
    category = models.ForeignKey(ArtCategory, on_delete=models.CASCADE,null=False,blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False,blank=False)
    image = models.ImageField(upload_to=art_directory_stor_path,default="art_image/default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    __user_like_dislike = None

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

    @property
    def number_of_likes(self):
        find = ArtLikeDislike.objects.filter(artist_art=self,like_dislike=True)
        return find.count()

    @property
    def number_of_dislikes(self):
        find = ArtLikeDislike.objects.filter(artist_art=self,like_dislike=False)
        return find.count()
    
    def current_user_like_dislike(self,user_info):
        find = ArtLikeDislike.objects.filter(artist_art=self,user=user_info)
        if not find:
            find = None
            pass
        self.__user_like_dislike = find
        return find

    def current_art_comment(self):
        find = ArtComment.objects.filter(artist_art=self)
        if not find:
            find = None
            pass
        return find


class ArtLikeDislike(models.Model):

    artist_art = models.ForeignKey(ArtistArt, on_delete=models.CASCADE,null=False,blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False,blank=False)
    like_dislike = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.artist_art.title
    
    def save(self, *args, **kwargs):
        find = ArtLikeDislike.objects.filter(user=self.user , artist_art=self.artist_art)
        if find:
            get_data = find.get()
            if get_data.like_dislike !=  self.like_dislike:
                find.update(like_dislike = self.like_dislike)
            else:
                # Same value as previous like
                pass
        else:
            super().save(*args, **kwargs)
            
        

class ArtComment(models.Model):

    artist_art = models.ForeignKey(ArtistArt, on_delete=models.CASCADE,null=False,blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False,blank=False)
    comment_message = models.CharField(max_length=255,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_message

