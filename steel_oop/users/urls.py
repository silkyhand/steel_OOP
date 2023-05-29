from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy

from . import views

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='products/index.html'),
        name='logout'
    ),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),

    path(
        'password-change/',
        views.PasswordChangeView.as_view(
            template_name='users/password_change.html',
            success_url=reverse_lazy('products:index'),),
        name='password_change'
    ),
    path('profile/<str:username>/', views.profile, name='profile'),
]
