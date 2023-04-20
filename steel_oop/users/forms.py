from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'username')


class ChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)


