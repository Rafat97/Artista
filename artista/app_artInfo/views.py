from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views import View
from register.models import User
from artistArt.models import ArtistArt, ArtComment
from artista.utils import get_current_user
import django_filters
from django import forms
from django.db import models
from django.shortcuts import get_object_or_404
from artistArt.forms import ArtCommentForm
from django.contrib import messages


class ProductFilter(django_filters.FilterSet):

    STATUS_CHOICES = (
        ("view_count", 'View Count ASC'),
        ("-view_count", 'View Count DESC'),
        ("-id", 'Recent Uploaded'),
    )

    search = django_filters.CharFilter(label="Search",max_length=255 , method='search__in')
    ordering = django_filters.ChoiceFilter(label="Ordering" , method='filter_by_order',choices=STATUS_CHOICES)

    class Meta:
        model = ArtistArt
        fields = ['category']

    def filter_by_order(self, queryset, value, name):
        if name:
            expression = name
            queryset = queryset.order_by(expression)
        return queryset
        
    def search__in(self, queryset, value, name):
        if name:
            expression = name
            queryset = queryset.filter(title__contains=expression)
        return queryset



# Create your views here.
class AllArtSearchView(View):
    def get(self, request, *args, **kwargs):
        user = get_current_user(request)
        if not user:
            return redirect('/')

        user = get_current_user(request)
        f = ProductFilter(  
                    request.GET, 
                    queryset=ArtistArt.objects.filter(post_status = "public")
                )
        context = {
            'user_info': user,
            'filter': f
        }
        return render(request, "all_art_preview_search.html", context)

    def post(self, request, *args, **kwargs):
        pass



# Create your views here.
class AllArtView(View):
    """
    Display an Artist Account

    **Context**

    ``mymodel``
        An instance of :model:`myapp.User`.

    **Template:**

    :template:`all_art_preview.html`
    """
    def get(self, request, *args, **kwargs):
        user = get_current_user(request)
        if not user:
            return redirect('/')

        art = ArtistArt.objects.filter(post_status = "public")

        context = {
            'user_info': user,
            "allArts" : art,
        }
        return render(request, "all_art_preview.html", context)

    def post(self, request, *args, **kwargs):
        pass


# Create your views here.
class SingleArtView(View):
    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uuid')
        if not uid:
            raise Http404("Page not found")

        art = get_object_or_404(
            ArtistArt,  uuid=uid,post_status='public'
        )
        user = get_current_user(request)
        if not user:
            return redirect('/')

        art.view_count = art.view_count + 1
        art.save()
        ART_INFO = art

        is_liked = False
        data =  ART_INFO.current_user_like_dislike(user)
        if data:
            is_liked = data.get().like_dislike
        
        comment = ART_INFO.current_art_comment()
        form = ArtCommentForm(None)

        context = {
            'user_info': user,
            'art_info': ART_INFO,
            'current_user_liked': is_liked,
            'art_comments': comment,
            'art_comments_form': form,
        }
        return render(request, "single_art_preview.html", context)

    def post(self, request, *args, **kwargs):
        pass


# Create your views here.
class SingleArtComment(View):


    
    def post(self, request, *args, **kwargs):
        uid = kwargs.get('image_uuid')
        typ = kwargs.get('type')
        if not uid:
            raise Http404("Page not found")
        if not typ:
            raise Http404("Page not found")
        user = get_current_user(request)
        if not user:
            return redirect('/')
        if typ == "delete":
            comment_id = request.POST.get("comment_id")
            comment = get_object_or_404(
                ArtComment,  id=comment_id
            )
            comment.delete()
            messages.error(request , " Comment is deleted")

        elif typ == "add" :
            art = get_object_or_404(
                ArtistArt,  uuid=uid,post_status='public'
            )
            form = ArtCommentForm(request.POST)
            form.setUser(user)
            form.setArt(art)

            if form.is_valid() :
                form.save(commit=True)

            else :
                messages.error(request , " Please give correct comment ")

        return redirect("app_artInfo:artist_single_art_page",uid)
