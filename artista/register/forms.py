from django import forms
from .models import User, Role
from django.contrib.auth.hashers import make_password, check_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class ClientUserForm(forms.ModelForm):
    """
    Client User register form

    **Super Class**

        from django import forms

    **Method User:**

        clean_confirm_password(self,current_user): \n
        def save(self, commit=True):return register.User \n


    ** Generated Form Field **

            'display_name',\n
            'email',\n
            'password',\n

    **Models that are used by this Class**

        The instance of model register.User.\n

    """
    display_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': '', }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': '', }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': '', }
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': '', }
    ))
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
        clientRole, created = Role.objects.get_or_create(role_name="Client")
        client_user.user_role = clientRole
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
        ]


class ArtistUserForm(forms.ModelForm):
    """
    Artist User register form

    **Super Class**

        from django import forms

    **Method User:**

        clean_confirm_password(self,current_user): \n
        def save(self, commit=True):return register.User \n


    ** Generated Form Field **

            'display_name',\n
            'email',\n
            'password',\n
            'confirm_password',\n
            'address',\n
            'phoneNumber',\n

    **Models that are used by this Class**

        The instance of model register.User.\n

    """
    display_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': '', }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': '', }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': '', }
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': '', }
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': '', }
    ), required=False)
    phoneNumber = forms.CharField(label="Phone Number", widget=forms.TextInput(
        attrs={'class': '', }
    ), required=False)
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
        artistRole, created = Role.objects.get_or_create(role_name="Artist")
        artist_user.user_role = artistRole
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
        ]

# not needed


class AdminUserForm(forms.ModelForm):
    CLIENT = 'client'
    ARTIST = 'artist'

    ROLE = (
        (CLIENT, 'Client'),
        (ARTIST, 'Artist')
    )
    #display_name=forms.CharField(widget=forms.TextInput() ,required=True)
    # email=forms.CharField(widget=forms.EmailInput(),required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    # password = ReadOnlyPasswordHashField(
    #     label=_("Password"),
    #     help_text=_(
    #         'Raw passwords are not stored, so there is no way to see this '
    #         'user’s password, but you can change the password using '
    #         '<a href="{}">this form</a>.'
    #     ),
    # )
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    # address=forms.CharField(widget=forms.TextInput())
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
