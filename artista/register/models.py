from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password
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
    path = 'avatar/user_{1}/avatar/{0}/{2}'.format(
        formatedDate, instance.id, filename)
    return path


class Role(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    role_name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.role_name


class User(models.Model):
    """
    Stores a single User entry.This is main User table .
    It's related to :model:`Role` 
    """
    CLIENT = 'client'
    ARTIST = 'artist'

    ROLE = (
        (CLIENT, 'Client'),
        (ARTIST, 'Artist')
    )
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False,
                            help_text="Auto Genarate Universally unique identifier ")
    display_name = models.CharField(
        max_length=30, blank=False, help_text="User display name")
    email = models.EmailField(
        unique=True, blank=False,  help_text="User Email")
    password = models.CharField(
        max_length=255, blank=False, help_text="User password")
    # current_password = models.CharField(max_length=255,blank=False)
    phoneNumber = models.CharField(
        max_length=20, null=True, blank=True, help_text="User Phone Number")
    address = models.CharField(
        max_length=255, null=True, blank=True, help_text="User Address")
    short_bio = models.CharField(
        max_length=255, null=True, blank=True, help_text="Short Bio")
    # user_role = models.CharField(max_length=255,null=False,choices=ROLE)
    # user_role = models.ForeignKey(Role, on_delete=models.CASCADE,null=False)
    user_role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    refresh_token = models.CharField(
        max_length=255, null=True, blank=True,  help_text="This is for forget password")
    avatar = models.ImageField(upload_to=user_directory_path,
                               default="avatar/default.jpg", help_text="User Profile Picture")
    is_active = models.BooleanField(
        default=True,  help_text="User is active or not default true")
    created_at = models.DateTimeField(
        auto_now_add=True,  help_text="User created time")

    @classmethod
    def from_db(cls, db, field_names, values):
        # print(cls,db,field_names,values)
        instance = super().from_db(db, field_names, values)
        instance._state.adding = False
        instance._state.db = db
        instance._field_names = (field_names)
        instance._old_values = dict(zip(field_names, values))
        return instance

    """ Check update request or not """

    def data_changed(self, fields):
        if hasattr(self, '_old_values'):
            for field in fields:
                if getattr(self, field) != self._old_values[field]:
                    return True

            return False

    def clean(self):
        if self.is_active == False:
            self.is_active = True

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
        else:
            if self.data_changed(self._field_names):
                super().save(*args, **kwargs)
                print("Data Change")
            else:
                print("No Data Change")
            pass

    def __str__(self):
        return self.email
