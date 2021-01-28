from django.urls import path
from .views import (RegistrationView, UsernameValidation, EmailValidation,
                    VerificationView, LoginView, LogoutView)
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('validate/username', csrf_exempt(UsernameValidation.as_view()), name="validate_username"),
    path('validate/email', csrf_exempt(EmailValidation.as_view()), name="validate_email"),
    path('verify/<uidb64>/<token>', VerificationView.as_view(), name="verify")
]
