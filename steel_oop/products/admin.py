from adminsortable.admin import SortableAdmin
from django.contrib import admin

from .models import Category, Product, Productlist, ProductNotlist, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_cat', 'slug', 'discount',)
    search_fields = ('name_cat',)
    list_editable = ('discount',)
    prepopulated_fields = {'slug': ('name_cat',)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug',)
    search_fields = ('name',)
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(SortableAdmin):
    list_display = ('subcategory', 'size', 'parameter', 'thickness', 'length',
                    'weight_item', 'area', 'price_tonn',
                    'price_item', 'coeff', 'base_price',
                    )
    search_fields = ('size',)
    list_filter = (('subcategory', admin.RelatedOnlyFieldListFilter),
                   )
    list_editable = ('base_price',)

    fieldsets = (
        ('Общие данные', {
            'fields': ('subcategory', 'size', 'parameter', 'thickness',
                       'length', 'area',
                       'coeff', 'base_price',
                       )
        }),
        ('Рассчитываемы данные', {
            'fields': ('weight_item', 'price_tonn', 'price_item')
        }),
    )


@admin.register(Productlist)
class ProductListAdmin(SortableAdmin):
    list_display = ('subcategory', 'thickness', 'size', 'weight_item', 'area',
                    'price_tonn',
                    'price_item', 'coeff', 'base_price',
                    )
    search_fields = ('thickness',)
    list_filter = (('subcategory', admin.RelatedOnlyFieldListFilter),
                   )
    list_editable = ('base_price',)

    def get_queryset(self, request):
        return Productlist.objects.exclude(thickness__isnull=True)

    fieldsets = (
        ('Общие данные', {
            'fields': ('subcategory', 'thickness', 'size', 'area',
                       'coeff', 'base_price',
                       )
        }),
        ('Рассчитываемы данные', {
            'fields': ('weight_item', 'price_tonn', 'price_item')
        }),
    )


@admin.register(ProductNotlist)
class ProductNotListAdmin(SortableAdmin):
    list_display = ('subcategory', 'size', 'parameter', 'length',
                    'weight_item',
                    'price_tonn',
                    'price_item',
                    'coeff',
                    'base_price',
                    )
    search_fields = ('size',)
    list_filter = (('subcategory', admin.RelatedOnlyFieldListFilter),
                   )
    list_editable = ('base_price',)

    def get_queryset(self, request):
        return Productlist.objects.exclude(thickness__isnull=False)

    fieldsets = (
        ('Общие данные', {
            'fields': ('subcategory', 'size', 'parameter', 'length',
                       'coeff', 'base_price',
                       )
        }),
        ('Рассчитываемы данные', {
            'fields': ('weight_item', 'price_tonn', 'price_item')
        }),
    )
