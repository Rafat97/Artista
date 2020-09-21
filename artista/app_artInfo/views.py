from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from register.models import User
from artistArt.models import ArtistArt, ArtComment, ArtLikeDislike
from artista.utils import get_current_user
import django_filters
from django import forms
from django.db import models
from django.shortcuts import get_object_or_404
from artistArt.forms import ArtCommentForm
from django.contrib import messages
from django.db.models import Q
from artistFollowing.models import ArtistFollow


class ProductFilter(django_filters.FilterSet):
    """

    Custom made filtering class . Filter the arts and show then in the website  .

    **Super Class**
        from django_filters import FilterSet

    **Method User:**

        filter_by_order(self, queryset, value, name): return queryset\n
        search__in(self, queryset, value, name):return queryset\n

     **Models that are used by this Class**

        The instance of model artistArt.ArtistArt.\n


    """

    STATUS_CHOICES = (
        ("view_count", 'View Count ASC'),
        ("-view_count", 'View Count DESC'),
        ("-id", 'Recent Uploaded'),
    )

    search = django_filters.CharFilter(
        label="Search", max_length=255, method='search__in')
    ordering = django_filters.ChoiceFilter(
        label="Ordering", method='filter_by_order', choices=STATUS_CHOICES)

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
            queryset = queryset.filter(
                Q(title__icontains=expression) |
                Q(tags__icontains=expression) |
                Q(short_description__icontains=expression)|
                Q(category__category_name__icontains=expression)
            )
        return queryset


# Create your views here.
class AllArtSearchView(View):
    """

    Search all the arts by filtering them .the filters are bacically categorywise filter,choosing viewcount or latest uploded. Also can search by title or parial title.

    **Super Class**

        from django.views import View

    **Method User:**

       GET

    **Context**

        user_info: register.User.\n
        filter: app_artinfo.View.ProductFilter.\n

    **Models that are used by this Class**

        The instance of model register.User.\n
        The instance of model artistArt.ArtistArt.\n

    **Template:**

        View Templates directory: artistArt/templates/all_art_preview_search.html
    """

    def get(self, request, *args, **kwargs):
        user = get_current_user(request)
        if not user:
            return redirect('/')

        user = get_current_user(request)
        f = ProductFilter(
            request.GET,
            queryset=ArtistArt.objects.filter(post_status="public")
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

    Display all the artist's public arts

    **Super Class**

        from django.views import View

    **Method User:**

       GET

    **Context**

        user_info: register.User.\n
        "allArts": artistArt.ArtistArt.\n

    **Models that are used by this Class**

        The instance of model register.User.\n
        The instance of model artistArt.ArtistArt.\n

    **Template:**

        View Templates directory: artistArt/templates/all_art_preview.html
    """

    def get(self, request, *args, **kwargs):
        user = get_current_user(request)
        if not user:
            return redirect('/')

        art = ArtistArt.objects.filter(post_status="public")

        context = {
            'user_info': user,
            "allArts": art,
        }
        return render(request, "all_art_preview.html", context)


# Create your views here.
class SingleArtView(View):
    """
    Displaing a specific art with comment, react, artist info etc

    **Super Class**

        from django.views import View

    **Method User:**

       GET

    **Context**

        'user_info': registe.User,\n
        'art_info': artistArt.ArtistArt,\n
        'current_user_liked': artistArt.ArtLikeDislike,\n
        'art_comments': artistArt.ArtComment,\n
        'art_comments_form': ArtCommentForm.form,\n
        'is_current_user_following': artistFollowing.ArtistFollow\n

    **Models that are used by this Class**

        The instance of model register.User.\n
        The instance of model artistArt.ArtistArt.\n
        The instance of model artistArt.ArtLikeDislike.\n
        The instance of model artistArt.ArtComment.\n
        The instance of model artistFollowing.ArtistFollow.\n

    **Template:**

        View Templates directory: app_artInfo\\templates\single_art_preview.html
    """

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uuid')
        if not uid:
            raise Http404("Page not found")

        art = get_object_or_404(
            ArtistArt,  uuid=uid, post_status='public'
        )
        user = get_current_user(request)
        if not user:
            return redirect('/')

        art.view_count = art.view_count + 1
        art.save()
        ART_INFO = art

        is_liked = False
        data = ART_INFO.current_user_like_dislike(user)
        if data:
            is_liked = data.get().like_dislike

        is_current_user_following = False
        data = ArtistFollow.objects.filter(
            user_following=ART_INFO.user)
        if data:
            is_current_user_following = True

        comment = ART_INFO.current_art_comment()
        form = ArtCommentForm(None)

        context = {
            'user_info': user,
            'art_info': ART_INFO,
            'current_user_liked': is_liked,
            'art_comments': comment,
            'art_comments_form': form,
            'is_current_user_following': is_current_user_following,
        }
        return render(request, "single_art_preview.html", context)

    def post(self, request, *args, **kwargs):
        pass


# Create your views here.
class SingleArtComment(View):
    """
    Comment submission using a form

    **Super Class**

        from django.views import View

    **Method User:**

        POST


    **Models that are used by this Class**

        The instance of model register.User.\n
        The instance of model artistArt.ArtComment.\n

    **Redirect to:**
        artist_single_art_page
    """

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
            messages.error(request, " Comment is deleted")

        elif typ == "add":
            art = get_object_or_404(
                ArtistArt,  uuid=uid, post_status='public'
            )
            form = ArtCommentForm(request.POST)
            form.setUser(user)
            form.setArt(art)

            if form.is_valid():
                form.save(commit=True)

            else:
                messages.error(request, " Please give correct comment ")

        return redirect("app_artInfo:artist_single_art_page", uid)


class ArtistArtReact(View):
    """
    React on a existing public art.Record the react 

    **Super Class**

        from django.views import View

    **Method User:**

        POST


    **Models that are used by this Class**

        The instance of model register.User.\n
        The instance of model artistArt.ArtLikeDislike.\n

    **Redirect to:**
        artist_single_art_page
    """

    USER_INFO = None
    ART_INFO = None

    def post(self, request, *args, **kwargs):
        uid = kwargs.get('uuid')
        if not uid:
            raise Http404("Page not found")

        self.USER_INFO = get_current_user(request)

        if self.USER_INFO == None:
            return redirect('/logout')

        art = ArtistArt.objects.get(uuid=uid)
        saveData = ArtLikeDislike()
        saveData.artist_art = art
        saveData.user = self.USER_INFO
        saveData.save()

        return redirect("app_artInfo:artist_single_art_page", uid)


class ArtistArtReactAllArt(View):
    """
    Show all the reacted art of currently logged-in user

    **Super Class**

        from django.views import View

    **Method User:**

        GET

    **Context**

        user_info: register.user,\n
        allLovedArts: artistArt.ArtLikeDislike,\n

    **Models that are used by this Class**

        The instance of model register.User.\n
        The instance of model artistArt.ArtistArt.\n

    **Template:**

        View Templates directory: artistArt/templates/all_reacted_art.html
    """

    def get(self, request, *args, **kwargs):

        user = get_current_user(request)

        all_Loved_Arts = ArtLikeDislike.objects.filter(
            Q(user=user), Q(like_dislike=True))

        context = {
            'user_info': user,
            "allLovedArts": all_Loved_Arts,
        }

        return render(request, "all_reacted_art.html", context)
