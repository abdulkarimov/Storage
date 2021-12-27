from rest_framework import serializers
from storage_model.models import Product


class ProductSerializer(serializers.Serializer):
    image = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=20)
    price = serializers.IntegerField()
    count = serializers.IntegerField()
    category = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.text)
        instance.name = validated_data.get('name', instance.text)
        instance.price = validated_data.get('price', instance.text)
        instance.count = validated_data.get('count', instance.text)
        instance.category = validated_data.get('category', instance.text)
        instance.save()
        return instance
