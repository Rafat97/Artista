from django import forms
from .models import ArtistReview
from django.utils.translation import gettext, gettext_lazy as _



class ArtistReviewForm(forms.ModelForm):
    __user_reviewing = None
    __user_reviewer = None

    def setUserReviewing(self,current_reviewing):
        self.__user_reviewing = current_reviewing

    def setUserReviewer(self,current_reviewer):
        self.__user_reviewer = current_reviewer

    def clean(self):
        if self.__user_reviewing != None and self.__user_reviewer != None and self.__user_reviewing == self.__user_reviewer:
            raise forms.ValidationError(_(" You can not review own. "))
       
        if self.__user_reviewing.user_role.role_name != 'Artist':
            raise forms.ValidationError(
                _(" You can not reviewing without Artist . "))


    def save(self, commit=True):
        art = super(ArtistReviewForm, self).save(commit=False)
        art.user_reviewing = self.__user_reviewing
        art.user_reviewer = self.__user_reviewer
        if commit:
            art.save()
        return art
    
    class Meta:
        model = ArtistReview
        fields = [
            'message',
        ]
