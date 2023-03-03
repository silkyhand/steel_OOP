# from django.contrib import admin

# from . models import Category, Product, ProductSpecificationValue, Subcategory, Specification


# class SpecificationValueInline(admin.TabularInline):
#     model = ProductSpecificationValue
#     min_num = 1
#     extra = 0


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name_cat',)
#     search_fields = ('name_cat',)
#     # list_editable = ('name_cat',)
#     empty_value_display = '-пусто-'


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('subcategory', 'show_specifications', 'base_price', 'discount',)
#     search_fields = ('subcategory',)
#     list_filter = ('subcategory',)
#     # list_editable = ('base_price', 'discount',)
#     empty_value_display = '-пусто-'
#     inlines = (
#         SpecificationValueInline,
#     )

#     def show_specifications(self, obj):
#         specification_list = []
#         for specification in obj.specifications.all():
#             specification_list.append(specification.name)
#         return specification_list



# @admin.register(ProductSpecificationValue)
# class ProductSpecificationValueAdmin(admin.ModelAdmin):
#     list_display = ('product', 'specification', 'value',)
#     search_fields = ('product',)
#     # list_editable = ('value',)
#     empty_value_display = '-пусто-'


# @admin.register(Subcategory)
# class SubcategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category',)
#     search_fields = ('name',)
#     # list_editable = ('slug',)
#     empty_value_display = '-пусто-'


# @admin.register(Specification)
# class SpecificationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'subcategory',)
#     search_fields = ('name',)
#     # list_editable = ('name',)
#     empty_value_display = '-пусто-'
