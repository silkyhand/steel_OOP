from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm

User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('products:index')
    template_name = 'users/signup.html'


def profile(request, username):
    buyer = get_object_or_404(User, username=username)
    user_orders = buyer.orders.all()
    context = {
        'buyer': buyer,
        'user_orders': user_orders,
    }
    return render(request, 'users/profile.html', context)
