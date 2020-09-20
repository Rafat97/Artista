from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
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

# Create your views here.


# Create your views here.
class UsersProfileEdit(View):
    def get(self, request, *args, **kwargs):
        user = get_current_user(request)
        if not user:
            return redirect('/')

        context = {
            'user_info': user,
        }
        return render(request, "user_profile_edit.html", context)

    def post(self, request, *args, **kwargs):
        pass
