from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category', 'product_pic')
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product_version', 'name_version', 'number_version', 'active_version',)
