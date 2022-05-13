from django.urls import path

from .views import (
    CreateCartsView,
    FinalizeCartsView,
    ListCartsView,
    ListCartsByCustomerView,
    UpdateCartsView,
    DeleteCartsView
)

app_name = "carts"

urlpatterns = [
    path("create-cart", CreateCartsView.as_view(), name="create-cart"),
    path("list-cart", ListCartsView.as_view(), name="list-cart"),
    path("list-cart/<uuid:pk>", ListCartsByCustomerView.as_view(), name="list-cart-by-customer"),
    path("update-cart/<uuid:pk>", UpdateCartsView.as_view(), name="update-cart"),
    path("delete-cart/<uuid:pk>", DeleteCartsView.as_view(), name="delete-cart"),
    path("finalize-cart/<uuid:pk>", FinalizeCartsView.as_view(), name="finalize-cart"),
]
