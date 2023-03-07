from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Collection, Product, Type, Lookbook, ProductImage

class ProductImageInline(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Collection)
admin.site.register(Lookbook)
admin.site.register(Type)



