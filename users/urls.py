from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, reset_password, email_verification, LoginView, LogoutView

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('verification/', email_verification, name='verification'),
    path('reset_password/', reset_password, name='reset_password'),
]