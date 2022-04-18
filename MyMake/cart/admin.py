from django.contrib import admin

from cart.models import Carts

# Register your models here.
class CartsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "customer",
    ]
    

admin.site.register(Carts, CartsAdmin)
