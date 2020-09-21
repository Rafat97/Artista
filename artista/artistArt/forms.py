from django import forms
from .models import ArtCategory, ArtistArt, ArtComment
from django.utils.translation import gettext, gettext_lazy as _


class ArtistArtViewForm(forms.ModelForm):
    """
    A form that generates Custom form to upload a art

    **Super Class**

        from django import forms

    **Method User:**

        clean_image(self): raise forms.ValidationError\n
        def clean(self): raise forms.ValidationError()\n
        save(self, commit=True): return add_art\n
        getUser(self): \n
        setUser(self): \n


    **Models that are used by this Class**

        The instance of model register.User.\n
        The instance of model artistArt.ArtistArt\n
        The instance of model artistArt.ArtCategory as FK\n


    ** Generated Form Field **

        image,\n
        title,\n
        short_description,\n
        long_description,\n
        tags,\n
        category,\n
        post_status\n

    """

    image = forms.ImageField(required=True)
    title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': '', }), required=True)
    short_description = forms.CharField(max_length=299, widget=forms.Textarea(
        attrs={'class': '', }), required=True)
    long_description = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={'class': '', }), required=True)

    __user = None

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 1*1024*1024:
                raise forms.ValidationError("Image file too large ( > 1mb )")
            return image
        else:
            raise forms.ValidationError("Couldn't read uploaded image")

    def clean(self):
        cleaned_data = super().clean()
        user = self.__user
        if user:
            if user.user_role.role_name != 'Artist':
                raise forms.ValidationError(
                    _('You are not allow upload a new art'))
        else:
            raise forms.ValidationError(
                _('You must logged in to upload a new art'))

    def save(self, commit=True):
        add_art = super(ArtistArtViewForm, self).save(commit=False)
        add_art.user = self.__user
        if commit:
            add_art.save()
        return add_art

    @property
    def getUser(self):
        return self.__user

    def setUser(self, current_user):
        self.__user = current_user

    class Meta:
        model = ArtistArt
        fields = [
            'image',
            'title',
            'short_description',
            'long_description',
            'tags',
            'category',
            'post_status'
        ]
        exclude = ['user', 'view_count']


class ArtCommentForm(forms.ModelForm):
    """
    A form that generates Custom form to comment a art

    **Super Class**

        from django import forms

    **Method User:**

        setUser(self,current_user): \n
        def setArt(self, current_art) \n
        def save(self, commit=True):return comment_art \n 



    **Models that are used by this Class**

        The instance of model register.User.\n
        The instance of model artistArt.ArtComment\n
        The instance of model artistArt.ArtCategory as FK\n


    ** Generated Form Field **

        comment_message\n


    """
    __user = None
    __art = None

    def setUser(self, current_user):
        self.__user = current_user

    def setArt(self, current_art):
        self.__art = current_art

    def save(self, commit=True):
        comment_art = super(ArtCommentForm, self).save(commit=False)
        comment_art.user = self.__user
        comment_art.artist_art = self.__art
        if commit:
            comment_art.save()
        return comment_art

    class Meta:
        model = ArtComment
        fields = [
            'comment_message',
        ]
