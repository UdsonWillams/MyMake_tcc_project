from django.contrib import admin

# Register your models here.
from products.models import Products
class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "price",
    ]
    readonly_fields=('cart_quantity',)

admin.site.register(Products, ProductsAdmin)
