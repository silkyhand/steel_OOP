from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .forms import CreationForm, UserPasswordChangeForm

User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('products:index')
    template_name = 'users/signup.html'


class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    """
    Изменение пароля пользователя
    """
    form_class = UserPasswordChangeForm
    template_name = 'modules/system/authenticated/password-change.html'
    success_message = 'Ваш пароль был успешно изменён!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение пароля на сайте'
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'slug': self.request.user.username})    


def profile(request, username):
    buyer = get_object_or_404(User, username=username)
    user_orders = buyer.orders.all()    
    context = {
        'buyer': buyer,        
        'user_orders': user_orders,
    }
    return render(request, 'users/profile.html', context)     
