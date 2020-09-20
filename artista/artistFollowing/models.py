from django.db import models
from register.models import User


# Create your models here.


class ArtistFollow(models.Model):

    user_following = models.ForeignKey(
        User, related_name='user_following', on_delete=models.SET_NULL, null=True)
    user_follower = models.ForeignKey(
        User, related_name='user_follower', on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.user_follower

    def save(self, *args, **kwargs):
        find = ArtistFollow.objects.filter(
            user_follower=self.user_follower, user_following=self.user_following)
        print(find)

        if find:
            get_data = find.get()
            get_data.delete()
        else:
            super().save(*args, **kwargs)
