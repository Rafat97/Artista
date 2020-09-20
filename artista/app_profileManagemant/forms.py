from django import forms
from register.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.utils.translation import gettext, gettext_lazy as _
import uuid
from django.db.models import Q


class UserEditProfile(forms.ModelForm):

    email = forms.CharField(label="Email",
                            widget=forms.EmailInput(
                                attrs={'class': 'form-control cnr-rounded', }
                            ),
                            max_length=100, required=True)

    display_name = forms.CharField(label="Display name",
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form-control cnr-rounded', }
                                   ),
                                   max_length=30, required=True)

    address = forms.CharField(label="Address",
                              widget=forms.TextInput(
                                  attrs={
                                      'class': 'form-control cnr-rounded', }
                              ),
                              max_length=255, required=True)

    phoneNumber = forms.CharField(label="Phone Number",
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control cnr-rounded', }
                                  ),
                                  max_length=20, required=True)

    avatar = forms.ImageField(label="Profile Picture", required=True)

    def clean_image(self):
        image = self.cleaned_data.get('avatar')
        if image:
            if image.size > 1*1024*1024:
                raise forms.ValidationError("Image file too large ( > 1mb )")
            return image
        else:
            raise forms.ValidationError("Couldn't read uploaded image")

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()

    def save(self, commit=True):
        usr = super(UserEditProfile, self).save(commit=False)
        if commit:
            usr.save()
        return usr

    class Meta:
        model = User
        fields = [
            'display_name',
            'email',
            'phoneNumber',
            'address',
            'avatar',
        ]
