from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, Http404
from django.views import View
from artista.utils import get_current_user
from htmlmin.decorators import minified_response
from django.shortcuts import get_object_or_404

from .models import ArtistFollow
from register.models import User

from django.db.models import Q

# Create your views here.


class ArtistFollowView(View):

    USER_INFO = None

    def get(self, request):
        self.USER_INFO = get_current_user(request)

        if self.USER_INFO == None:
            return redirect('/logout')

        artists = ArtistFollow.objects.filter(
            user_follower=self.USER_INFO)

        # artists = User.objects.filter(
        #     Q(user_role_id=1) & ~Q(uuid=self.USER_INFO.uuid))

        if self.USER_INFO == None:
            return redirect('/logout')
        context = {
            'artists': artists,
            'user_info': self.USER_INFO
        }

        return render(request, 'follow.html', context)

    # def post(self, request):
    #     self.USER_INFO = get_current_user(request)

    #     artist_id = request.POST.get('artist_id')

    #     artist_user = get_object_or_404(User,  uuid=artist_id)

    #     print("Current User =", self.USER_INFO)
    #     print("Current User following =", artist_user.uuid)

    #     return redirect('artist_follow')


class ArtistFollowViewFormSubmit(View):

    USER_INFO = None

    def post(self, request, *args, **kwargs):

        prev_url = request.META['HTTP_REFERER']

        following_uid = kwargs.get('uuid')
        if not following_uid:
            raise Http404("Page not found")

        art = request.POST.get('art')

        self.USER_INFO = get_current_user(request)
        if self.USER_INFO == None:
            return redirect('/logout')

        artist_user = get_object_or_404(
            User,  uuid=following_uid
        )
        af = ArtistFollow()
        af.user_follower = self.USER_INFO
        af.user_following = artist_user
        af.save()

        # {% url 'app_artInfo:artist_single_art_page'  data.uuid %}

        return redirect(prev_url)
