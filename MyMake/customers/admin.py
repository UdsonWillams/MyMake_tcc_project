from django.contrib import admin

from customers.models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "is_active",
    ]
    

admin.site.register(Customer, CustomerAdmin)
