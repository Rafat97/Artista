from django import forms
from .models import ArtCategory,ArtistArt,ArtComment
from django.utils.translation import gettext, gettext_lazy as _


class ArtistArtViewForm(forms.ModelForm):

    image = forms.ImageField(required=True)
    title=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control cnr-rounded',}) , required=True )
    short_description = forms.CharField(max_length=299, widget=forms.Textarea(attrs={'class':'form-control cnr-rounded',}), required=True )
    long_description = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class':'form-control cnr-rounded',}), required=True )
  
    __user = None

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size> 1*1024*1024:
                raise forms.ValidationError("Image file too large ( > 1mb )")
            return image
        else:
            raise forms.ValidationError("Couldn't read uploaded image")     

    def clean(self):
        cleaned_data = super().clean()
        user = self.__user
        if user:
            if user.user_role.role_name != 'Artist':
                raise forms.ValidationError(_('You are not allow upload a new art'))
        else:
            raise forms.ValidationError(_('You must logged in to upload a new art'))

  
    def save(self, commit=True):
        add_art = super(ArtistArtViewForm, self).save(commit=False)
        add_art.user = self.__user
        if commit:
            add_art.save()
        return add_art
        
    @property
    def getUser(self):
        return self.__user

    def setUser(self,current_user):
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
        exclude = ['user','view_count']



class ArtCommentForm(forms.ModelForm):
    __user = None
    __art = None

    def setUser(self,current_user):
        self.__user = current_user

    def setArt(self,current_art):
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
