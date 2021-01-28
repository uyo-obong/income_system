from .imports import *


class VerificationView(View):
    def get(self, request, uidb64, token):
        user_id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=user_id)

        try:
            if user.is_active:
                messages.success(request, 'Your account is already activated')
                return redirect('login')
            user.is_active = True
            user.save()
            messages.success(request, 'Your account as been activated')
            return redirect('login')

        except Exception as e:
            pass
        return redirect('login')
