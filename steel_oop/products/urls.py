from django.urls import path

from . import views


app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('subcategory/<slug:slug>/', views.subcategory_products, name='subcategory_products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
   ]    
# path('category/<cat_slug:slug>/<subcat_slug:slug>/',
#      views.products_subcategory, name='products_subcategory'
#      ),
# path('category/<cat_slug:slug>/', views.products_category,
#      name='products_category'
#      ),

