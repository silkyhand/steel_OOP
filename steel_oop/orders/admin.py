from django.contrib import admin

from .models import ProductInCart


@admin.register(ProductInCart)
class ProductInCartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInCart._meta.fields]
    

# class ProductInOrderInline(admin.TabularInline):
#     model = ProductInOrder
#     extra = 0


# @admin.register(Status)
# class StatusAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in Status._meta.fields]

    
# @admin.register(Order)
# class OrderAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in Order._meta.fields]
#     inlines = [ProductInOrderInline]


# @admin.register(ProductInOrder)   
# class ProductInOrderAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in ProductInOrder._meta.fields]
