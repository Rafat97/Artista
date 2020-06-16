from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import View
from artista.utils import get_current_user
from .forms import ArtistArtViewForm

class ArtistArtUploadNew(View):

    USER_INFO = None

    def get(self, request, *args, **kwargs):
        self.USER_INFO = get_current_user(request)
        if self.USER_INFO == None:
            return redirect('/logout')
        form = ArtistArtViewForm()
        context = {
            'user_info' : self.USER_INFO,
            'form' : form
        }    
        return render(request, 'artist_art_upload_form.html', context)

    def post(self, request, *args, **kwargs):
        self.USER_INFO = get_current_user(request)
        
        if self.USER_INFO == None:
            return redirect('/logout')

        form = ArtistArtViewForm(request.POST or None)
        form.setUser(current_user = self.USER_INFO)
        if form.is_valid() :
            data = form.save()
            print(data)
            return HttpResponse("Thank you to upload a new art")

        context = {
            'user_info' : self.USER_INFO,
            'form' : form
        }    
        return render(request, 'artist_art_upload_form.html', context)