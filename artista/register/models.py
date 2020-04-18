from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password,check_password
import uuid

class User(models.Model):
    CLIENT = 'client'
    ARTIST = 'artist'

    ROLE = (
        (CLIENT, 'Client'),
        (ARTIST, 'Artist')
    )
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    display_name = models.CharField(max_length=30,blank=False)
    email = models.EmailField(unique=True,blank=False)
    password = models.CharField(max_length=255,blank=False)
    phoneNumber = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    # user_role = models.ForeignKey(Role, on_delete=models.CASCADE,null=False)
    user_role = models.CharField(max_length=255,null=False,choices=ROLE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def artist_validaiton_role(self):
        if self.user_role == "artist":
            error = {}
            if not self.phoneNumber :
                error['phoneNumber'] = ValidationError(_('Missing artist phone.'))
            if not self.address :
                error['address'] = ValidationError(_('Missing artist address.'))
                # raise ValidationError({
                #     'address': ValidationError(_('Missing artist address.')),
                # })
            if error:
                raise ValidationError(error)
            pass

    def clean(self):
        self.password = make_password(self.password)
        if not self.user_role:
            raise ValidationError({
                'user_role': ValidationError(_('Missing user role.')),
            })
        self.artist_validaiton_role()
        if self.is_active == False:
           self.is_active = True
        

    # def save(self, *args, **kwargs):
    #     print(self.phoneNumber)
    #     super().save(*args, **kwargs)
       

    def __str__(self):
        return self.email

