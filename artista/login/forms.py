from django import forms
from register.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.utils.translation import gettext, gettext_lazy as _


class LoginFrom(forms.Form):

    """
    A form that generates Custom form to login a user

    **Super Class**

        from django import forms

    **Method User:**

        clean_email(self,current_user): \n
        def getUser(self, current_art) \n
        def save(self, commit=True):return register.User \n



    **Models that are used by this Class**

        The instance of model register.User.\n

    """

    email = forms.CharField(label="Email",
                            widget=forms.EmailInput(
                                attrs={'class': '', }
                            ),
                            max_length=100, required=True)

    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': '', }
    ), required=True)

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
            if check_password(password_not_hashed, user.password):
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
