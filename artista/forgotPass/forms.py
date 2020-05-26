from django import forms
from register.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.utils.translation import gettext, gettext_lazy as _
import uuid

class ForgotPassUserFrom(forms.Form):

    email=forms.CharField(label="Email" ,
    widget=forms.EmailInput(
        attrs={'class':'form-control cnr-rounded',}
    ),
    max_length=100 ,required=True)
    
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
            user.refresh_token = str(uuid.uuid4())
            user.save()
            self.__user = user
        else:
            raise forms.ValidationError(_('Invalid user email address'))
        
    @property
    def getUser(self):
        return self.__user
        
        # 
        # if check_password(password_not_hashed,password_hash):
            # pass
