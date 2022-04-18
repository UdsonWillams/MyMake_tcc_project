from products.models import Products
from cart.models import Carts
from rest_framework import serializers

class ProductsCartSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    quantity = serializers.CharField()
    class Meta:
        model = Products
        fields = [
            "name", 
            "quantity",
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
            quantity = value["quantity"]
            product = Products.objects.get(name=name)

            if int(quantity) <= 0:
                raise serializers.ValidationError("valores negativos não podem ser atribuidos")

            if int(quantity) > int(product.quantity):
                raise serializers.ValidationError("Quantidade maior que o estoque do produto")

        return values


    def create(self, validated_data):
        import ipdb
        ipdb.set_trace()
        customer = validated_data["customer"]
        
        for value in validated_data["products"]:
            products_name = value["name"]
            cart_products_quantity = value["quantity"]          

            old_quantity = Products.objects.get(name=products_name)
            old_quantity = old_quantity.quantity
            new_products_quantity = (int(old_quantity) - int(cart_products_quantity))
            Products.objects.filter(name=products_name).update(quantity=new_products_quantity)
        carts = Carts.objects.create(customer=customer, products=validated_data["products"])
        return carts


class ListCartsSerializer(serializers.Serializer):
    customer = serializers.UUIDField()
    products = serializers.CharField()
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
