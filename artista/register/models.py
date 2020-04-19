from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password,check_password
import uuid

from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import StringIO
import sys
from datetime import datetime

def user_directory_path(instance, filename):
    myDate = datetime.now()
    formatedDate = myDate.strftime("%Y-%m-%d")
    path = 'avatar/user_{1}/avatar/{0}/{2}'.format(formatedDate,instance.id, filename)
    return path


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
    # current_password = models.CharField(max_length=255,blank=False)
    phoneNumber = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    # user_role = models.ForeignKey(Role, on_delete=models.CASCADE,null=False)
    user_role = models.CharField(max_length=255,null=False,choices=ROLE)
    avatar = models.ImageField(upload_to=user_directory_path,default="avatar/default.jpg")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def from_db(cls, db, field_names, values):
        # print(cls,db,field_names,values)
        instance = super().from_db(db, field_names, values)
        instance._state.adding = False
        instance._state.db = db
        instance._field_names = (field_names)
        instance._old_values = dict(zip(field_names, values))
        return instance

    def data_changed(self, fields):
        if hasattr(self, '_old_values'):
            for field in fields:
                if getattr(self, field) != self._old_values[field]:
                    return True

            return False

    def artist_validaiton_role(self):
        if self.user_role == "artist":
            error = {}
            if not self.phoneNumber :
                error['phoneNumber'] = ValidationError(_('Missing artist phone.'))
            if not self.address :
                error['address'] = ValidationError(_('Missing artist address.'))
            if error:
                raise ValidationError(error)
            pass

    def clean(self):
        if not self.user_role:
            raise ValidationError({
                'user_role': ValidationError(_('Missing user role.')),
            })
        self.artist_validaiton_role()
        if self.is_active == False:
           self.is_active = True
        

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
        else:
            if self.data_changed(self._field_names):
                super().save(*args, **kwargs)
                print("Data Change")
            else :
                print("No Data Change")
            pass
       

    def __str__(self):
        return self.email
