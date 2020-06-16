from register.models import User
import re
from django.shortcuts import render,redirect
from django.http import Http404 ,HttpResponse
from django.core.exceptions import PermissionDenied
from django.urls import resolve

class MainMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        # print(response)
        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    def process_view(self,request, view_func, view_args, view_kwargs):
        #  request.session['user_id']
        # print(view_func.__name__)
        # print(view_args)
        # print(view_kwargs)
        # print(request.path)
        pass
        
    def process_exception(self,request, exception):
        print("process_exception")
        pass

    def process_template_response(self,request, response):
        '''
        It must return a response object that implements a render method.
        It could alter the given response by changing `response.template_name` and `response.context_data`,
        or it could create and return a brand-new TemplateResponse or equivalent
        '''
        # print("process_template_response")
        return response    



class CustomAuthMiddleware:

    LOG_REQUIRED_URL = [
        "/dashboard/"
    ]
    USER_LOGIN_REDIRECT_NAME = [
        "login_user",
        "register_client",
        "register_artist",
    ]

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print(resolve( request.path_info ).url_name)
        # exit
        user_uuid = None
        if request.session.has_key('user'):
            user_uuid = request.session['user']
            user = User.objects.filter(uuid__exact=user_uuid)
            if not user:
                response = redirect('logout_user')
                return response
            else:
                for url in self.USER_LOGIN_REDIRECT_NAME:
                    if url == resolve( request.path_info ).url_name :
                        # print("TRUE")
                        return redirect('/dashboard')

        else:
            for url in self.LOG_REQUIRED_URL:
                # print(url,request.path,re.search(url, request.path))
                    if re.search(url, request.path):
                        raise Http404("Page not found")
                       


        response = self.get_response(request)
        # print(response)
        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    def process_view(self,request, view_func, view_args, view_kwargs):
        #  request.session['user_id']
        # print(view_func.__name__)
        # print(view_args)
        # print(view_kwargs)
        # print(request.path)
        # print(request.resolver_match)
        pass
        
    def process_exception(self,request, exception):
        print("process_exception")
        pass

    def process_template_response(self,request, response):
        '''
        It must return a response object that implements a render method.
        It could alter the given response by changing `response.template_name` and `response.context_data`,
        or it could create and return a brand-new TemplateResponse or equivalent
        '''
        # print("process_template_response")
        return response    


        