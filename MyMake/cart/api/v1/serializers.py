from products.models import Products
from cart.models import Carts
from rest_framework import serializers
from customers.models import Customer
class ProductsCartSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    cart_quantity = serializers.CharField()
    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "cart_quantity",
        ]


class CreateCartsSerializer(serializers.ModelSerializer):

    products = ProductsCartSerializer(many=True)
    
    class Meta:
        model = Carts
        fields = [
            "id",
            "customer", 
            "products",
        ]

    def validate_products(self, values):
        for value in values:
            name = value["name"]
            quantity = value["cart_quantity"]
            try:
                product = Products.objects.get(name=name)
            except Exception:
                raise serializers.ValidationError("Produto não encontrado!")
            if int(quantity) <= 0:
                raise serializers.ValidationError("valores negativos não podem ser atribuidos")

            if int(quantity) > int(product.quantity):
                raise serializers.ValidationError("Quantidade maior que o estoque do produto")

        return values

    def validate_customer(self, value):
        if Carts.objects.filter(customer_id=value.id).exists():
            raise serializers.ValidationError("cliente já possui um carrinho!!!")
        return value

    def create(self, validated_data):
        customer = validated_data["customer"]
        list_of_products = []

        for value in validated_data["products"]:
            products_name = value["name"]
            cart_products_quantity = value["cart_quantity"]          

            product = Products.objects.get(name=products_name)
            old_quantity = product.quantity
            new_products_quantity = (int(old_quantity) - int(cart_products_quantity))
            Products.objects.filter(name=products_name).update(quantity=new_products_quantity, cart_quantity=cart_products_quantity)
            list_of_products.append(product)
        carts = Carts(customer=customer)
        carts.save()

        for i in range(len(list_of_products)):
            prod = list_of_products[i]
            carts.products.add(prod)
        return carts


class ListCartsSerializer(serializers.Serializer):
    customer = serializers.UUIDField()
    products = ProductsCartSerializer(many=True)
    class Meta:
        model = Carts
        fields = [
            "customer",
            "products"
        ]
class ConcluirCartsSerializer(serializers.Serializer):
    products = ProductsCartSerializer(many=True)
    class Meta:
        model = Carts
        fields = [
            "products"
        ]

