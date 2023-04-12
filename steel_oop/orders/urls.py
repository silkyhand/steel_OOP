from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.cart_order, name='cart_order'),   
    path('adding/', views.cart_adding, name='cart_adding'), 
    path('update/', views.cart_update, name='cart_update'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
