from django.contrib import admin

# Register your models here.
from products.models import Products
class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "price",
    ]
    

admin.site.register(Products, ProductsAdmin)
