from django.contrib.auth.forms import UserChangeForm, UserCreationForm, SetPasswordForm

from .models import User


class CreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'username')


class ChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)


class UserPasswordChangeForm(SetPasswordForm):
    """
    Форма изменения пароля
    """
    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })
