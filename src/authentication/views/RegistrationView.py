from .imports import *


class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html', context={})

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])

        context = {'fieldData': request.POST}

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():

                if len(password) < 6:
                    messages.error(request, 'Password must be at least 6')
                    return render(request, 'authentication/register.html', context)

                user = User.objects.create(username=username, email=email, password=password)
                user.is_active = False
                user.save()

                self.send_verification_email(request, email, user)

                messages.success(request, 'Verification link has been sent to your email')
                return render(request, 'authentication/register.html', context={})

        return render(request, 'authentication/register.html', context={})

    def send_verification_email(self, request, email, user):
        subject = 'Action require! Verify your email'
        body = self.email_body(request, user)
        send_mail(subject, body, 'noreply@example.com', [email],  html_message=body, fail_silently=False)

    @staticmethod
    def email_body(request, user):
        domain = get_current_site(request).domain
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)
        link = reverse('verify', kwargs={'uidb64': uidb64, 'token': token})
        activate_link = 'http://'+domain + link

        return render_to_string('authentication/mail/activate.html', {
            'activate_link': activate_link, 'user': user
        })

