from django.urls import path, include
from . import views


urlpatterns = [
    path('artCategory', views.artCategory, name='category'),

    # path('architecture', views.architecture, name='architecture'),
    # path('ceramics', views.ceramics, name='ceramics'),
    # path('conceptualArt', views.conceptualArt, name='conceptualArt'),
    # path('drawing', views.drawing, name='drawing'),
    # path('painting', views.painting, name='painting'),
    # path('photography', views.photography, name='photography'),
    # path('sclpture', views.sclpture, name='sclpture'),

]
