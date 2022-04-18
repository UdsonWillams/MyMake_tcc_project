from django.urls import path

from .views import (
    CreateProductsView,
    ListProductsByNameView,
    ListProductsView,
    UpdateProductsView,
    DeleteProductsView
)

app_name = "products"

urlpatterns = [
    path("create-product", CreateProductsView.as_view(), name="create-product"),
    path("list-product", ListProductsView.as_view(), name="list-product"),
    path("list-product/<str>", ListProductsByNameView.as_view(), name="list-product-name"),
    path("update-product/<uuid:pk>", UpdateProductsView.as_view(), name="update-product"),
    path("delete-product/<uuid:pk>", DeleteProductsView.as_view(), name="delete-product"),
]