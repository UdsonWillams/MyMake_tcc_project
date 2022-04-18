from django.urls import path

from .views import (
    CreateCustomerView,
    UpdateCustomerView,
    ListCustomerView,
    ListCustomerByEmailView,
)

app_name = "customers"

urlpatterns = [
    path("create-user", CreateCustomerView.as_view(), name="create-user"),
    path("list-user", ListCustomerView.as_view(), name="list-user"),
    path("list-user/email", ListCustomerByEmailView.as_view(), name="list-user"),
    path("update-user/<int:pk>", UpdateCustomerView.as_view(), name="list-user"),
]