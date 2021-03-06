from .imports import *


class UsernameValidation(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should not contain alphanumeric'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Oops! username already taken'}, status=409)

        return JsonResponse({'username_valid': True})


class EmailValidation(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is not valid'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Oops! email already taken'}, status=409)

        return JsonResponse({'email_valid': True})