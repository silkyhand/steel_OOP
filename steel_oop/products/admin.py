from django.contrib import admin

from .models import Category, ProductList, ProductNotList, Subcategory


# class SubCategoryListFilter(admin.SimpleListFilter):
#     title = ('Категории товаров')
#     parameter_name = 'subcategory'
    
#     def lookups(self, request, model_admin):
#         (
#             ('listovoy', ('листовой')),
#             ('sortovoy', ('сортовой')),
#             ('prokat_trub', ('прокат труб')),
#         )

#     def queryset(self, request, queryset):
#         if self.value() == 'listovoy':
#             return queryset.filter(category.slug == 'listovoy')               
#             )
#         if self.value() == '90s':
#             return queryset.filter(
#                 birthday__gte=date(1990, 1, 1),
#                 birthday__lte=date(1999, 12, 31),
#             )    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_cat', 'slug',)
    search_fields = ('name_cat',)
    # list_editable = ('name_cat',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug',)
    search_fields = ('name',)
    list_filter = ('category',)
    list_editable = ('slug',)
    

@admin.register(ProductNotList)
class ProductNotListAdmin(admin.ModelAdmin):
    list_display = ('size', 'parameter', 'length', 'show_price_tonn',
                    'show_price_metr', 'coeff', 'base_price', 'discount',
                    )
    search_fields = ('size',)
    list_filter = (('subcategory', admin.RelatedOnlyFieldListFilter),
    )
    list_editable = ('base_price', 'discount',)

    def show_price_tonn(self, obj):
        return obj.price_tonn

    def show_price_metr(self, obj):
        return obj.price_metr


@admin.register(ProductList)
class ProductListAdmin(admin.ModelAdmin):
    list_display = ('thickness', 'size', 'area', 'show_price_tonn',
                    'show_price_item', 'coeff', 'base_price', 'discount',
                    )
    search_fields = ('thickness',)
    list_filter = (('subcategory', admin.RelatedOnlyFieldListFilter),
    )
    list_editable = ('base_price', 'discount',)

    def show_price_tonn(self, obj):
        return obj.pricetonn

    def show_price_item(self, obj):
        return obj.priceitem
