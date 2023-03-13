from django.contrib import admin

from .models import Category, Product, Productlist, ProductNotlist, Subcategory


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
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('size', 'parameter', 'thickness', 'length', 'area', 'price_tonn',
                    'price_item', 'coeff', 'base_price', 'discount',
                    )
    search_fields = ('size',)
    list_filter = (('subcategory', admin.RelatedOnlyFieldListFilter),
                   )
    list_editable = ('base_price', 'discount',)

    # def price_tonn(self, obj):
    #     return obj.price_tonn
    # price_tonn.short_description = 'Цена за тонну'

    # def price_metr(self, obj):
    #     return obj.price_metr
    # price_metr.short_description = 'Цена за метр'


@admin.register(Productlist)
class ProductListAdmin(admin.ModelAdmin):
    list_display = ('subcategory','thickness', 'size', 'area', 'price_tonn',
                    'price_item', 'coeff', 'base_price', 'discount',
                    )
    search_fields = ('thickness',)
    list_filter = (('subcategory', admin.RelatedOnlyFieldListFilter),
                   )
    list_editable = ('base_price', 'discount',)

    def get_queryset(self, request):
        return Productlist.objects.exclude(thickness__isnull=True)

    def price_item(self):
        return self.price_item

    price_item.short_description = 'Цена за штуку'


@admin.register(ProductNotlist)
class ProductNotListAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'size', 'parameter', 'length', 'price_tonn',
                    'price_item', 'coeff', 'base_price', 'discount',
                    )
    search_fields = ('size',)
    list_filter = (('subcategory', admin.RelatedOnlyFieldListFilter),
                   )
    list_editable = ('base_price', 'discount',)

    def get_queryset(self, request):
        return Productlist.objects.exclude(thickness__isnull=False)

    def price_item(self, obj):
        return obj.price_item

    price_item.short_description = 'Цена за погонный метр'
    
# @admin.register(ProductList)
# class ProductListAdmin(admin.ModelAdmin):
#     list_display = ('thickness', 'size', 'area', 'price_tonn',
#                     'price_item', 'coeff', 'base_price', 'discount',
#                     )
#     search_fields = ('thickness',)
#     list_filter = (('subcategory', admin.RelatedOnlyFieldListFilter),
#                    )
#     list_editable = ('base_price', 'discount',)

    # def price_tonn(self, obj):
    #     return obj.price_tonn

    # def price_item(self, obj):
    #     return obj.price_item

    # price_tonn.short_description = 'Цена за тонну'
    # price_item.short_description = 'Цена за штуку'