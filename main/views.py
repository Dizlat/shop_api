from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .filters import ProductFilter
from main.models import *
from  .serializers import *

# 1. Список товаров, доступен всем пользователям
@api_view(['GET'])
def product_list(request):
    queryset = Product.objects.all()
    filtered = ProductFilter(request.GET, queryset=queryset)
    serializer = ProductListSerializer(filtered.qs, many=True)
    serializer_queryset = serializer.data
    return Response(data=serializer_queryset, status=status.HTTP_200_OK)


# 2. Дутали товаров, доступен всем
# 3. Создание товаров, рудактирование, удаление, доступно только админам
# 4. Создание отзывов, доступно только залогиненным пользователям
# 5. Листинг отзывов (внутри деталей продукта) доступен всем
# 6. Редактр и удаление отзыва может делать только автор
# 7. Заказ может создать любой залогиненый пользователь
# 8. Список заказов: пользователь может видит только свои заказы, админы видят все
# 9. редактр заказы может только админ

