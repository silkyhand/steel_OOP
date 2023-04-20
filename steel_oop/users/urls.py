from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView, PasswordChangeDoneView                                    
                                      
from django.urls import path

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
        PasswordChangeView.as_view(template_name='users/password_change.html'),
        name='password_change'
    ),
    path(
        'password-change/done/',
        PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
        name='password_change_done'
    ),
    path('profile/<str:username>/', views.profile, name='profile'),
]