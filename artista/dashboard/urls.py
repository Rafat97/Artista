from django.urls import path ,include
from .views import DashboardView


app_name="dashboard"
urlpatterns = [
    path('', DashboardView.as_view(), name='default_dashboard_home'), #landing page url
]