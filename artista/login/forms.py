from django import forms
from register.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.utils.translation import gettext, gettext_lazy as _

class LoginFrom(forms.Form):

    email=forms.CharField(label="Email", widget=forms.EmailInput(),max_length=100 ,required=False)
    password=forms.CharField(label="Password", widget=forms.PasswordInput(),required=False)

    __user = None

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email").lower()
        password_not_hashed = cleaned_data.get("password")
        user = User.objects.filter(email__exact=email)
        if user:
            user = user.get()
            if check_password(password_not_hashed,user.password):
                self.__user = user
                pass
            else:
                raise forms.ValidationError(_('Invalid user credentials'))
        else:
            raise forms.ValidationError(_('Invalid user credentials'))
        
    @property
    def getUser(self):
        return self.__user
        
        # 
        # if check_password(password_not_hashed,password_hash):
            # pass
