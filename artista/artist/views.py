from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views import View
from artista.utils import get_current_user
from register.models import User
from django.shortcuts import get_object_or_404
from artistArt.models import ArtistArt, ArtComment
from artist.forms import ArtistReviewForm

from .models import ArtistReview
from django.db.models import Q
from django.contrib import messages

# Create your views here.


class DashboardArtistView(View):
    """
    Show all the art that has been uploaded by currently logger-in user

    **Super Class**

        from django.views import View

    **Method User:**

        GET

    **Models that are used by this Class**

        The instance of model register.User.\n


    **Template**
    View Templates directory: artist/templates/home.html

    """
    USER_INFO = None

    def get(self, request, *args, **kwargs):
        self.USER_INFO = get_current_user(request)

        if self.USER_INFO.user_role.role_name != 'Artist':
            return redirect('/dashboard')

        if self.USER_INFO == None:
            return redirect('/logout')
        context = {
            'user_info': self.USER_INFO
        }
        return render(request, "home.html", context)


class SingleArtistView(View):
    """
    Show the informations of a single Artist .Artist's short Bio, reviews etx

    **Super Class**

        from django.views import View

    **Method User:**

        GET

    **Models that are used by this Class**

        The instance of model register.User.\n
        The instance of model artistArt.ArtistReview\n
        The instance of model artistArt.ArtistArt\n


    **COntext**
        user_info: register.user,
        artist_info: register.user,
        artist_review: artistArt.ArtistReview,
        arts_info: artistArt.ArtistArt,  


    **Template**
    View Templates directory: artist/templates/single_artist_view.html

    """
    USER_INFO = None

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uuid')
        if not uid:
            raise Http404("Page not found")

        self.USER_INFO = get_current_user(request)

        if self.USER_INFO == None:
            return redirect('/logout')

        artist_user = get_object_or_404(
            User,  uuid=uid
        )
        artist_all_art = ArtistArt.objects.filter(
            Q(user=artist_user), Q(post_status='public'))

        artist_reviews = ArtistReview.objects.filter(
            Q(user_reviewer=artist_user), Q(post_status='public')).order_by('-id')

        context = {
            'user_info': self.USER_INFO,
            'artist_info': artist_user,
            'artist_review': artist_reviews,
            'arts_info': artist_all_art,
        }
        return render(request, "single_artist_view.html", context)


class ArtistReviewView(View):
    """
    Submit a Review through a form

    **Super Class**

        from django.views import View

    **Method User:**

        POST

    **Models that are used by this Class**

        The instance of model register.User.\n
        The instance of model artistArt.ArtistReview\n
        The instance of model artistArt.ArtistArt\n



    **Redirect**
        View Redirect Url name: artist:single_artist_info

    """
    USER_INFO = None

    def post(self, request, *args, **kwargs):
        reviewing_uid = kwargs.get('uuid')
        if not reviewing_uid:
            raise Http404("Page not found")

        message = request.POST.get('message')

        self.USER_INFO = get_current_user(request)
        if self.USER_INFO == None:
            return redirect('/logout')

        artist_user = get_object_or_404(
            User,  uuid=reviewing_uid
        )
        form = ArtistReviewForm(request.POST)
        form.setUserReviewing(self.USER_INFO)
        form.setUserReviewer(artist_user)

        if form.is_valid():
            form.save(commit=True)
        else:
            messages.error(request, " Please give correct review message ")

        return redirect("artist:single_artist_info", reviewing_uid)
