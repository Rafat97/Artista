from django.urls import path ,include
from .views import UsersProfileEdit

app_name="app_profileManagemant"
urlpatterns = [
    path('', UsersProfileEdit.as_view(), name='home'), #landing page url
]