from django import forms
from .models import *

class ClientUserForm(forms.ModelForm):
    # display_name=forms.CharField(widget=forms.TextInput())
    # email=forms.CharField(widget=forms.EmailInput())
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    # address=forms.CharField(widget=forms.TextInput())
    # phone=forms.CharField(widget=forms.TextInput())
    # is_active = forms.CharField(widget=forms.CheckboxInput())

    def clean_confirm_password(self):
        cleaned_data = super(ClientUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm password does not match"
            )

    class Meta:
        model = User
        fields = [
            'display_name',
            'email',
            'address',
            'phoneNumber',
            'user_role',
            'is_active',
        ]