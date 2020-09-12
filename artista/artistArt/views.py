from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, Http404
from django.views import View
from artista.utils import get_current_user
from .forms import ArtistArtViewForm
from htmlmin.decorators import minified_response
from .models import ArtCategory, ArtistArt, ArtComment, ArtLikeDislike
from django.shortcuts import get_object_or_404

class ArtistArtUploadNew(View):

    USER_INFO = None

    def get(self, request, *args, **kwargs):
        self.USER_INFO = get_current_user(request)
        if self.USER_INFO == None:
            return redirect('/logout')
        form = ArtistArtViewForm(None)
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
            # return HttpResponse("Thank you to upload a new art code is = "+str(data.uuid))
            return redirect('artist_own_all_art')

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
        
        art = get_object_or_404(
            ArtistArt,  uuid=uid,post_status='public'
        )
        
        # ArtistArt.objects.get(
        #     uuid=uid,
        #     post_status='public'
        # ) 
        print("sadasdasdasd")
        
        if not art:
            raise Http404("Page not found")

        art.view_count = art.view_count + 1
        art.save()
        self.ART_INFO = art
        self.USER_INFO = get_current_user(request)

        if self.USER_INFO == None:
            return redirect('/logout')
            
        is_liked = None
        data =  self.ART_INFO.current_user_like_dislike(self.USER_INFO)
        if data:
            is_liked = data.get().like_dislike

        context = {
            'user_info': self.USER_INFO,
            'art_info': self.ART_INFO,
            'current_user_liked': is_liked,
        }
        return render(request, 'artist_art_preview.html', context)


class ArtistArtUploadEdit(View):

    USER_INFO = None

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uuid')
        if not uid:
            raise Http404("Page not found")
        self.USER_INFO = get_current_user(request)
        if self.USER_INFO == None:
            return redirect('/logout')

        art = get_object_or_404(
            ArtistArt,  uuid=uid,user=self.USER_INFO
        )   

        form = ArtistArtViewForm(instance=art)
        context = {
            'user_info': self.USER_INFO,
            'form': form
        }
        return render(request, 'artist_art_upload_form.html', context)

    def post(self, request, *args, **kwargs):
        uid = kwargs.get('uuid')
        if not uid:
            raise Http404("Page not found")
        self.USER_INFO = get_current_user(request)

        if self.USER_INFO == None:
            return redirect('/logout')
        art = get_object_or_404(
            ArtistArt,  uuid=uid,user=self.USER_INFO
        ) 

        form = ArtistArtViewForm(request.POST, request.FILES or None, instance=art)
        form.setUser(current_user=self.USER_INFO)
        if form.is_valid():
            data = form.save()
            return redirect('artist_own_all_art')

        context = {
            'user_info': self.USER_INFO,
            'form': form
        }
        return render(request, 'artist_art_upload_form.html', context)


class ArtistArtUploadedDelete(View):

    USER_INFO = None

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uuid')
        if not uid:
            raise Http404("Page not found")
        self.USER_INFO = get_current_user(request)

        if self.USER_INFO == None:
            return redirect('/logout')
        art = get_object_or_404(
            ArtistArt,  uuid=uid,user=self.USER_INFO
        ) 
        art.delete()
        return redirect('artist_own_all_art')

        
class ArtistArtPreviewAll(View):

    USER_INFO = None
    ART_INFO = None

    def get(self, request, *args, **kwargs):

        self.USER_INFO = get_current_user(request)

        if self.USER_INFO == None:
            return redirect('/logout')

        art = ArtistArt.objects.filter( user=self.USER_INFO)  
        self.ART_INFO = art

        context = {
            'user_info': self.USER_INFO,
            'arts_info': self.ART_INFO,
        }
        return render(request, 'artist_all_art_preview.html', context)

