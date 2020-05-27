from django.urls import path ,include
from .views import ForgotPassword,ForgotPasswordReset


urlpatterns = [
    path('', ForgotPassword.as_view(),name='forgot_password_user'), 
    path('reset/<slug:user_uuid>/<slug:user_reset_token>',  ForgotPasswordReset.as_view() ,name='forgot_password_user_reset_form'),
]