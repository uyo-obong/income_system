from django.contrib import auth

from .imports import *


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('index')
            messages.error(request, 'username or password is invalid')
            return render(request, 'authentication/login.html')
        messages.error(request, 'Input field can not be empty')
        return render(request, 'authentication/login.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        return redirect('login')
