from django.contrib import admin
from .models import Category, Product, ProductImage
from django.utils.translation import ugettext as _

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['image_tag',]
    extra = 3
    verbose_name = _('Product Image')
    verbose_name_plural = _('Products Image')

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'image_tag', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['image_tag']
    inlines = [ProductImageInline,]


admin.site.register(Product, ProductAdmin)

