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
from .forms import UserEditProfile

# Create your views here.


# Create your views here.
class UsersProfileEdit(View):
    """
    Edit the profile of currently logged-in user

    **Super Class**

        from django.views import View

    **Method User:**

        GET,POST

    **Context**

        user_info: register.user,\n
        form: app_profileManagement.form.UserEditProfile\n    

    **Models that are used by this Class**

        The instance of model register.User.\n


    **Template:**

        View Templates directory: app_profileManagement/templates/user_profile_edit.html
    """

    def get(self, request, *args, **kwargs):
        user = get_current_user(request)
        if not user:
            return redirect('/logout')
        form = UserEditProfile(instance=user)
        context = {
            'user_info': user,
            'form': form
        }
        return render(request, "user_profile_edit.html", context)

    def post(self, request, *args, **kwargs):
        user = get_current_user(request)
        if not user:
            return redirect('/logout')

        form = UserEditProfile(
            request.POST, request.FILES or None, instance=user)

        if form.is_valid():
            data = form.save()
            return redirect('app_profileManagemant:home')

        context = {
            'user_info': user,
            'form': form
        }
        return render(request, 'user_profile_edit.html', context)
