from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from htmlmin.decorators import minified_response


def blaBla(request, *args, **kwargs):
    return render(request, 'blabla.html', {})


def blaBlaadd(request, *args, **kwargs):
    print(request.GET)
    x1 = request.GET.get('num1', 0)
    x2 = request.GET.get('num2', 0)
    Y = int(x1) + int(x2)
    return HttpResponse(Y)

# class base view


class HomePageView(View):
    """

    Landing Page View

    **Super Class**

        from django.views import View

    **Method User:**

       GET

    **Template:**

        View Templates directory: getStart/templates/landing_page.html
    """

    @minified_response
    def get(self, request, *args, **kwargs):
        request.session['app_name'] = "Artista"
        # del request.session['app_name']
        return render(request, 'landing_page.html', {})

# function base view


@minified_response
def home_view(request, *args, **kwargs):
    return render(request, 'landing_page.html', {})
