from django.urls import path

from .views import (
    CreateCartsView,
    FinalizeCartsView,
    ListCartsView,
    ListCartsByIdView,
    UpdateProductsView,
    DeleteCartsView
)

app_name = "carts"

urlpatterns = [
    path("create-cart", CreateCartsView.as_view(), name="create-cart"),
    path("list-cart", ListCartsView.as_view(), name="list-cart"),
    path("list-cart/<uuid:pk>", ListCartsByIdView.as_view(), name="list-cart"),
    path("update-cart/<uuid:pk>", UpdateProductsView.as_view(), name="update-user"),
    path("delete-cart/<uuid:pk>", DeleteCartsView.as_view(), name="delete-cart"),
    path("finalize-cart/<uuid:pk>", FinalizeCartsView.as_view(), name="finalize-cart"),
]
