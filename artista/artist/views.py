from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views import View
from artista.utils import get_current_user
from register.models import User
from django.shortcuts import get_object_or_404
from artistArt.models import ArtistArt, ArtComment
from django.db.models import Q

# Create your views here.


class DashboardArtistView(View):
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
    USER_INFO = None

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uuid')
        if not uid:
            raise Http404("Page not found")

        self.USER_INFO = get_current_user(request)

        if self.USER_INFO.user_role.role_name != 'Artist':
            return redirect('/dashboard')

        if self.USER_INFO == None:
            return redirect('/logout')

        artist_user = get_object_or_404(
            User,  uuid=uid
        )
        artist_all_art = ArtistArt.objects.filter(
            Q(user=artist_user), Q(post_status='public'))

        context = {
            'user_info': self.USER_INFO,
            'artist_info': artist_user,
            'arts_info': artist_all_art,
        }
        return render(request, "single_artist_view.html", context)
