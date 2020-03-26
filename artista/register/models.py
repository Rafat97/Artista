from django.db import models
from django import forms



class User(models.Model):
    CLIENT = 'client'
    ARTIST = 'artist'

    ROLE = (
        (CLIENT, 'Client'),
        (ARTIST, 'Artist')
    )
    display_name = models.CharField(max_length=30,blank=False)
    email = models.EmailField(unique=True,blank=False)
    password = models.CharField(max_length=255,blank=False)
    phoneNumber = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=255,null=True)
    # user_role = models.ForeignKey(Role, on_delete=models.CASCADE,null=False)
    user_role = models.CharField(max_length=255,null=False,choices=ROLE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

