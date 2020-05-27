from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import View
from .forms import ForgotPassUserFrom
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

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
            html_message = render_to_string('email/forgot_password_email.html', 
            {
                'user': user,
                "site_url" : settings.SITE_URL,
                "pass_recov_url" : settings.SITE_URL+"forgot_password/reset"+"/"+str(user.uuid)+"/"+user.refresh_token
            })
            
            mail = send_mail(
                'Password Recovery' ,
                "",
                'no-reply@artista.com',
                [user.email],
                html_message=html_message,
            )
            # return HttpResponse("bla bla ")
            if mail:
                messages.success(request, 'Please check your email.')
                # return HttpResponse("Please check your email ! ")
            else:
                messages.error(request, 'Please ! Try again or Contact us.')

        response = redirect('forgot_password_user')
        return response






class ForgotPasswordReset(View):
    def get(self, request,user_uuid,user_reset_token, *args, **kwargs):
        
        return HttpResponse(user_uuid + "<br>" + user_reset_token)