from django.db import models
from register.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ArtistReview(models.Model):
    STATUS = (
        ('public', 'Public'),
        ('private', 'Private')
    )

    user_reviewing = models.ForeignKey(
        User, related_name='user_reviewing', on_delete=models.SET_NULL, null=True)
    user_reviewer = models.ForeignKey(
        User, related_name='user_reviewer', on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=255, blank=False)
    post_status = models.CharField(
        max_length=20, null=False, choices=STATUS, default='public')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.message
