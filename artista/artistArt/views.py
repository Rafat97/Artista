from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, Http404
from django.views import View
from artista.utils import get_current_user
from .forms import ArtistArtViewForm
from htmlmin.decorators import minified_response
from .models import ArtCategory, ArtistArt, ArtComment, ArtLikeDislike


class ArtistArtUploadNew(View):

    USER_INFO = None

    def get(self, request, *args, **kwargs):
        self.USER_INFO = get_current_user(request)
        if self.USER_INFO == None:
            return redirect('/logout')
        form = ArtistArtViewForm()
        context = {
            'user_info': self.USER_INFO,
            'form': form
        }
        return render(request, 'artist_art_upload_form.html', context)

    def post(self, request, *args, **kwargs):
        self.USER_INFO = get_current_user(request)

        if self.USER_INFO == None:
            return redirect('/logout')

        form = ArtistArtViewForm(request.POST, request.FILES or None)
        form.setUser(current_user=self.USER_INFO)
        if form.is_valid():
            data = form.save()
            print(data)
            return HttpResponse("Thank you to upload a new art code is = "+str(data.uuid))

        context = {
            'user_info': self.USER_INFO,
            'form': form
        }
        return render(request, 'artist_art_upload_form.html', context)


class ArtistArtPreview(View):

    USER_INFO = None
    ART_INFO = None

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uuid')
        if not uid:
            raise Http404("Page not found")
        art = ArtistArt.objects.get(
            uuid=uid,
            post_status='public'
        )
        if not art:
            raise Http404("Page not found")

        art.view_count = art.view_count + 1
        art.save()
        self.ART_INFO = art
        self.USER_INFO = get_current_user(request)

        if self.USER_INFO == None:
            return redirect('/logout')
            
        current_user_liked = False
        find = ArtLikeDislike.objects.filter(user=self.USER_INFO, artist_art=self.ART_INFO)
        if find:
            current_user_liked = True
        context = {
            'user_info': self.USER_INFO,
            'art_info': self.ART_INFO,
            'current_user_liked': current_user_liked,
        }
        return render(request, 'artist_art_preview.html', context)
