from rest_framework import serializers

from customers.models import Customer

class CreateCustomerSerializer(serializers.Serializer):
    name  = serializers.CharField()
    email = serializers.EmailField()
    password  = serializers.CharField()
    
    class Meta:        
        fields = [
        "name",
        "email",
        "password"
    ]
    model = Customer

class ListCustomerSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    total_spend = serializers.IntegerField()
    class Meta:
        fields = [
            "name",
            "email",
            "total_spend",
        ]
        model = Customer

class ListCustomerSerializerByEmail(serializers.Serializer):
    email = serializers.CharField()
    class Meta:
        fields = [
            "email",
        ]
        model = Customer
    
    def validate_email(self, value):
        if Customer.objects.filter(email=value).exists():
            return value 
        raise ValueError("Email não Encontrado!")
        
class UpdateCustomerSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    password  = serializers.CharField()
    class Meta:
        fields = [
            "name",
            "email",
            "password",
        ]
        model = Customer

    def update(self, instance, validated_data):
        instance.username = validated_data.get('name', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
