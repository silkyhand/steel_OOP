from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(blank=True, null=True, max_length=50)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
