from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('', include('products.urls', namespace='products')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
]
