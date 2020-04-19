from django import forms
from .models import User
from django.contrib.auth.hashers import make_password,check_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class ClientUserForm(forms.ModelForm):
    # display_name=forms.CharField(widget=forms.TextInput())
    # email=forms.CharField(widget=forms.EmailInput())
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    user_role = forms.CharField(label="", widget=forms.HiddenInput(), required = False, initial="client")
    # address=forms.CharField(widget=forms.TextInput(), required=False)
    # phone=forms.CharField(widget=forms.TextInput(), required=False)
    # is_active = forms.CharField(widget=forms.CheckboxInput())

    def clean_confirm_password(self):
        cleaned_data = super(ClientUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm password does not match"
            )
            
    def save(self, commit=True):
        client_user = super(ClientUserForm, self).save(commit=False)
        password = make_password(self.cleaned_data["password"])
        client_user.password = password
        if commit:
            client_user.save()

        return client_user
        

    class Meta:
        model = User
        fields = [
            'display_name',
            'email',
            'password',
            'user_role',
        ]

class ArtistUserForm(forms.ModelForm):
    # display_name=forms.CharField(widget=forms.TextInput())
    # email=forms.CharField(widget=forms.EmailInput())
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    address=forms.CharField(widget=forms.TextInput(),required = False)
    phoneNumber=forms.CharField(label="Phone Number", widget=forms.TextInput(),required = False )
    user_role = forms.CharField(label="", widget=forms.HiddenInput(), required = False, initial="artist")
    # is_active = forms.CharField(widget=forms.CheckboxInput())

    def clean_confirm_password(self):
        cleaned_data = super(ArtistUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm password does not match"
            )

    def save(self, commit=True):
        artist_user = super(ArtistUserForm, self).save(commit=False)
        password = make_password(self.cleaned_data["password"])
        artist_user.password = password
        if commit:
            artist_user.save()
        return artist_user

    class Meta:
        model = User
        fields = [
            'display_name',
            'email',
            'password',
            'confirm_password',
            'address',
            'phoneNumber',
            'user_role',
        ]



class AdminUserForm(forms.ModelForm):
    CLIENT = 'client'
    ARTIST = 'artist'

    ROLE = (
        (CLIENT, 'Client'),
        (ARTIST, 'Artist')
    )
    #display_name=forms.CharField(widget=forms.TextInput() ,required=True)
    #email=forms.CharField(widget=forms.EmailInput(),required=True)
    password=forms.CharField(widget=forms.PasswordInput())
    # password = ReadOnlyPasswordHashField(
    #     label=_("Password"),
    #     help_text=_(
    #         'Raw passwords are not stored, so there is no way to see this '
    #         'user’s password, but you can change the password using '
    #         '<a href="{}">this form</a>.'
    #     ),
    # )
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    #address=forms.CharField(widget=forms.TextInput())
    #phoneNumber=forms.CharField(label="Phone Number", widget=forms.TextInput())
    #user_role = forms.ChoiceField(label="Role", choices=ROLE ,  required=True)
    # is_active = forms.CharField(widget=forms.CheckboxInput())

    def clean_confirm_password(self):
        cleaned_data = super(AdminUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm password does not match"
            )

    def save(self, commit=True):
        artist_user = super(AdminUserForm, self).save(commit=False)
        password = make_password(self.cleaned_data["password"])
        artist_user.password = password
        if commit:
            artist_user.save()
        return artist_user      

    class Meta:
        model = User
        fields = [
            'display_name',
            'email',
            'password',
            'confirm_password',
            'address',
            'phoneNumber',
            'user_role',
        ]