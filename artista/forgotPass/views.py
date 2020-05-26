from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ForgotPassUserFrom
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.

class ForgotPassword(View):
    def get(self, request, *args, **kwargs):
        form = ForgotPassUserFrom(request.POST or None)
        context = {
            "form" : form
        }
        return render(request, 'forgot_password.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ForgotPassUserFrom(request.POST or None)
        if form.is_valid() :

            user = form.getUser
            # print(user.refresh_token)
            html_message = render_to_string('email/forgot_password_email.html', {'user': user,"site_url" : settings.SITE_URL})
            
            mail = send_mail(
                'Password Recovery' ,
                "",
                'no-reply@artista.com',
                [user.email],
                html_message=html_message,
            )
            # return HttpResponse("bla bla ")
            if mail:
                return HttpResponse("Please check your email ! ")

        context = {
            "form" : form
        }
        return render(request, 'forgot_password.html', context)