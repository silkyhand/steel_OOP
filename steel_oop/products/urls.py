from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'subcategory/<slug:slug>/',
        views.products_list,
        name='products_list'),
]
