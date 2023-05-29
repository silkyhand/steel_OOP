from django import forms
from django.contrib.auth import get_user_model

from .models import Order

User = get_user_model()


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'comments']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        if self.request and self.request.user.is_authenticated:
            self.fields['name'].initial = self.request.user.username
            self.fields['email'].initial = self.request.user.email
            self.fields['phone'].widget.attrs.update(
                {'placeholder': 'Телефон'})
            self.fields['comments'].widget.attrs.update(
                {'placeholder': 'Комментарий'})
        else:
            self.fields['name'].widget.attrs.update({'placeholder': 'Имя'})
            self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
            self.fields['phone'].widget.attrs.update(
                {'placeholder': 'Телефон'})
            self.fields['comments'].widget.attrs.update(
                {'placeholder': 'Комментарий'})
