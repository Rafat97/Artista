from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, Http404
from django.views import View
from artista.utils import get_current_user
from htmlmin.decorators import minified_response
from django.shortcuts import get_object_or_404


from register.models import User

from django.db.models import Q

# Create your views here.


class ArtistFollow(View):

    USER_INFO = None

    def get(self, request):
        self.USER_INFO = get_current_user(request)

        if self.USER_INFO == None:
            return redirect('/logout')

        artists = User.objects.filter(
            Q(user_role_id=1) & ~Q(uuid=self.USER_INFO.uuid))

        if self.USER_INFO == None:
            return redirect('/logout')
        context = {
            'artists': artists,
            'user_info': self.USER_INFO
        }

        return render(request, 'follow.html', context)

    def post(self, request):
        self.USER_INFO = get_current_user(request)

        artist_id = request.POST.get('artist_id')

        artist_user = get_object_or_404(User,  uuid=artist_id)

        print("Current User =", self.USER_INFO)
        print("Current User following =", artist_user.uuid)

        return redirect('artist_follow')
