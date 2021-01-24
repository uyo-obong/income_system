from django.urls import path
from .views import RegistrationView, UsernameValidation, EmailValidation
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('validate/username', csrf_exempt(UsernameValidation.as_view()), name="validate_username"),
    path('validate/email', csrf_exempt(EmailValidation.as_view()), name="validate_email")
]
