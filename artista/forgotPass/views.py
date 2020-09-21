from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import View
from .forms import ForgotPassUserFrom, ForgotPassNewPassSetUserFrom
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from register.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.


class ForgotPassword(View):
    """
    User Password reset using email send. 

    **Super Class**

        from django.views import View

    **Method :**

       GET,POST

    **Context**

       "getting email form": forgotPass.form.ForgotPassUserFrom

    **Models that are used by this Class**

        The instance of model register.User.\n


    **Template:**

        In get request View Templates directory: forgotPass\\templates\\forgot_password.html
        In Post request  reditect url name : forgot_password_user
    """

    def get(self, request, *args, **kwargs):
        form = ForgotPassUserFrom(request.POST or None)
        context = {
            "form": form
        }
        return render(request, 'forgot_password.html', context)

    def post(self, request, *args, **kwargs):
        form = ForgotPassUserFrom(request.POST or None)
        if form.is_valid():

            user = form.getUser
            # print(user.refresh_token)
            html_message = render_to_string('email/forgot_password_email.html',
                                            {
                                                'user': user,
                                                "site_url": settings.SITE_URL,
                                                "pass_recov_url": settings.SITE_URL+"forgot_password/reset"+"/"+str(user.uuid)+"/"+user.refresh_token
                                            })
            # email sending code
            mail = send_mail(
                'Password Recovery',
                "",
                'no-reply@artista.com',
                [user.email],
                html_message=html_message,
            )
            # return HttpResponse("bla bla ")
            if mail:
                messages.success(request, 'Please check your email. ')
                # return HttpResponse("Please check your email ! ")
            else:
                messages.error(request, 'Please ! Try again or Contact us.')

        response = redirect('forgot_password_user')
        return response


class ForgotPasswordReset(View):
    def get(self, request, user_uuid, user_reset_token, *args, **kwargs):
        user = get_object_or_404(
            User,  Q(uuid=user_uuid), Q(refresh_token=user_reset_token)
        )

        form = ForgotPassNewPassSetUserFrom(None)
        context = {
            "form": form
        }
        return render(request, 'forgot_password_form.html', context)

    def post(self, request, user_uuid, user_reset_token, *args, **kwargs):
        print("asdasd")
        pass
        form = ForgotPassNewPassSetUserFrom(request.POST or None)
        form.setToken(user_reset_token)
        form.setIdUser(user_uuid)
        if form.is_valid():
            form.save(commit=True)
            messages.success(
                request, " Your password is changed. Please login with new password ")
            response = redirect('login_user')
            return response

        context = {
            "form": form
        }
        return render(request, 'forgot_password_form.html', context)
