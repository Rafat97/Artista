from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from artista.utils import get_current_user

# Create your views here.


def artCategory(request):
    """

    a function based vied method to see all the category  and their arts.

    **Methot parameter **
        request

    **Context**
        user_info: register.User.\n


    **Models that are used by this Class**

        The instance of model register.User.\n


    **Template:**

        View Templates directory: artistArt/templates/artist_category.html
    """
    USER_INFO = get_current_user(request)

    if USER_INFO == None:
        return redirect('/logout')
    context = {
        'user_info': USER_INFO
    }
    return render(request, 'artist_category.html', context)


# def architecture(request):
#     return render(request, 'architecture.html')


# def ceramics(request):
#     return render(request, 'ceramics.html')


# def conceptualArt(request):
#     return render(request, 'painting.html')


# def drawing(request):
#     return render(request, 'drawing.html')


# def painting(request):
#     return render(request, 'painting.html')


# def photography(request):
#     return render(request, 'photography.html')


# def sclpture(request):
#     return render(request, 'sclpture.html')
