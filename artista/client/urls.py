from django.urls import path ,include
from .views import DashboardClientView


urlpatterns = [
    path('', DashboardClientView.as_view(), name='client_dashboard'), #landing page url
]