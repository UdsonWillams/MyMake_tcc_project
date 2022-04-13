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

class ListUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    class Meta:
        fields = [
            "name",
            "email",
        ]
        model = Customer

class UpdateUserSerializer(serializers.Serializer):
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
