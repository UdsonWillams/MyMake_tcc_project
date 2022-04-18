from rest_framework import serializers

from products.models import Products
class CreateProductsSerializers(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    category = serializers.CharField()

    class Meta:
        model = Products
        fields = [      
            "name",
            "price",
            "description",
            "quantity",
            "category",
        ]

    def validate_name(self, value):
        if Products.objects.filter(name=value).exists():
            raise serializers.ValidationError("Esse nome de produto já está sendo utilizado")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Não é possivel cadastrar produto com preço negativo")
        else:
            return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Não é possivel cadastrar produto com quantidade negativa")
        else:
            return value    

    def create(self, validated_data):
        products = Products.objects.create(**validated_data)
        return products

    
class ListProductsSerializers(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()

    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "price",
            "description",
            "quantity",
        ]

class UpdateProductsSerializers(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()

    class Meta:
        model = Products
        fields = [
            "name",
            "price",
            "description",
            "quantity",
        ]
      

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Não é possivel cadastrar produto com preço negativo")
        else:
            return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Não é possivel cadastrar produto com quantidade negativa")
        else:
            return value 

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

class DeleteProductsSerializer(serializers.Serializer):
    class Meta:
        model = Products
        fields = [
            "id"
        ]
