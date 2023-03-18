from django.urls import path

from . import views


app_name = 'products'

urlpatterns = [
<<<<<<< HEAD
    path('',  views.ProductListView.as_view(), name='index'),
=======
    path('', views.ProductListView.as_view(), name='index'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    
>>>>>>> 39229bdd952abfe75b981b1737b92b08fac99895
    # path('category/<cat_slug:slug>/<subcat_slug:slug>/',
    #      views.products_subcategory, name='products_subcategory'
    #      ),
    # path('category/<cat_slug:slug>/', views.products_category,
    #      name='products_category'
    #      ),
]
