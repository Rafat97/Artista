from django.urls import path ,include
from .views import DashboardClientView

app_name="client"
urlpatterns = [
    #path('', DashboardClientView.as_view(), name='home'), #landing page url
]