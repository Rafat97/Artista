from django import forms
from register.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.utils.translation import gettext, gettext_lazy as _
import uuid
from django.db.models import Q


class ForgotPassUserFrom(forms.Form):
    """
    A form that generates Custom form to Forgot Pass form

    **Super Class**

        from django import forms

    **Method User:**

        clean_email(self,current_user): \n
        getUser(self):return register.user \n
        clean(self, current_art) \n

    **Models that are used by this Class**

        The instance of model register.User.\n

    """

    email = forms.CharField(label="Email",
                            widget=forms.EmailInput(
                                attrs={'class': '', }
                            ),
                            max_length=100, required=True)

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


class ForgotPassNewPassSetUserFrom(forms.Form):
    """
    A form that generates to changeing user password  based on 

    **Super Class**

        from django import forms

    **Method User:**

        setToken(self,current_user): \n
        setIdUser(self) \n
        clean(self, current_art) \n
        clean_confirm_password(self, current_art) \n
        save(self, commit=True)

    **Models that are used by this Class**

        The instance of model register.User.\n

    """

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': '', }
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': '', }
    ))

    __user = None
    __token = None
    __iduser = None

    def setToken(self, token_user):
        self.__token = token_user

    def setIdUser(self, user_id):
        self.__iduser = user_id

    def clean_confirm_password(self):
        cleaned_data = super(ForgotPassNewPassSetUserFrom, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm password does not match"
            )

    def clean(self):
        cleaned_data = super().clean()
        if self.__token and self.__iduser:
            user = User.objects.get(
                Q(uuid=self.__iduser), Q(refresh_token=self.__token))
            if not user:
                raise forms.ValidationError(
                    _(' You are not allow to reset password '))
            else:
                password_not_hashed = self.cleaned_data["password"]
                if check_password(password_not_hashed, user.password):
                    raise forms.ValidationError(
                        _(' You can not use this password. Please use another one '))
                else:
                    self.__user = user
        else:
            raise forms.ValidationError(_(' Invalid reset password request '))

    def save(self, commit=True):
        password = make_password(self.cleaned_data["password"])
        self.__user.password = password
        self.__user.refresh_token = None
        if commit:
            self.__user.save()

        return self.__user
