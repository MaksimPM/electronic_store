import random
import string

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        token = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        user.token = token
        send_mail(
            subject='Подтверждение электронной почты',
            message=f'Код для подтверждения: {token}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_verified:
            return reverse('index')
        return reverse('users:verification')


class LogoutView(BaseLogoutView):
    pass


def email_verification(request):
    if request.method == 'POST':
        input_token = request.POST.get('key')
        try:
            user = User.objects.get(token=input_token)
            user.is_verified = True
            user.save()
        except User.DoesNotExist:
            return render(request, 'users/unsuccessful_verification.html')
        return render(request, 'users/successful_verification.html')
    return render(request, 'users/verification.html')


def reset_password(request):
    if request.method == 'POST':
        input_email = request.POST.get('email')
        user = User.objects.filter(email=input_email).first()
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save(update_fields=['password'])
        send_mail(
            subject='Сброс пароля',
            message=f'''Вы успешно сбросили пароль для аккаунта {input_email}.\n Ваш новый пароль: {password}''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[input_email]
        )

    return render(request, 'users/reset_password.html')
