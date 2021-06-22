from rest_framework import serializers

from main.models import *


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    pass


class OrderItemsSerializer(serializers.ModelSerializer):
    pass


class OrderSerializer(serializers.ModelSerializer):
    pass
