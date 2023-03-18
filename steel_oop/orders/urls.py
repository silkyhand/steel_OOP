from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url('', views.cart_detail, name='cart_detail'),
    url('add/<int:product_id>/', views.cart_add, name='cart_add'),
    url('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]