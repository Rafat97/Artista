from django.db import models
import uuid
from datetime import datetime
from register.models import User

# Create your models here.
class ArtCategory(models.Model):
   category_name=models.CharField(max_length=100,blank=False)

   def __str__(self):
        return self.category_name

def art_directory_stor_path(instance, filename):
    myDate = datetime.now()
    formatedDate = myDate.strftime("%Y-%m-%d")
    path = 'art_image/{0}/{1}'.format(formatedDate, filename)
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
    post_status = models.CharField(max_length=20,null=False,choices=STATUS,default='private')
    category = models.ForeignKey(ArtCategory, on_delete=models.CASCADE,null=False,blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False,blank=False)
    image = models.ImageField(upload_to=art_directory_stor_path,default="art_image/default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title