from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class ChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
