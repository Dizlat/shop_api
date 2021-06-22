from rest_framework import serializers

from main.models import *


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'image')


class ProductDetailSerializer(serializers.ModelSerializer):
    pass


class ReviewSerializer(serializers.ModelSerializer):
    pass


class OrderItemsSerializer(serializers.ModelSerializer):
    pass


class OrderSerializer(serializers.ModelSerializer):
    pass
