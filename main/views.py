import django_filters.rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets, status

from .filters import ProductFilter
from main.models import *
from .serializers import *
from .permissions import IsAuthorOrAdminPermission, DenyAll


# 1. Список товаров, доступен всем пользователям
# @api_view(['GET'])
# def product_list(request):
#     queryset = Product.objects.all()
#     filtered = ProductFilter(request.GET, queryset=queryset)
#     serializer = ProductListSerializer(filtered.qs, many=True)
#     serializer_queryset = serializer.data
#     return Response(data=serializer_queryset, status=status.HTTP_200_OK)


# class ProductListView(APIView):
#     def get(self, request):
#         queryset = Product.objects.all()
#         filtered = ProductFilter(request.GET, queryset=queryset)
#         serializer = ProductListSerializer(filtered.qs, many=True)
#         serializer_queryset = serializer.data
#         return Response(data=serializer_queryset, status=status.HTTP_200_OK)

#
# class ProductListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductListSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = ProductFilter


# 2. Дутали товаров, доступен всем
class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


# 3. Создание товаров, рудактирование, удаление, доступно только админам
# class CreateProductView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerializer
#     permission_classes = [IsAdminUser]
#
#
# class UpdateProductView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerializer
#     permission_classes = [IsAdminUser]
#
#
# class DeleteProductView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerializer
#     permission_classes = [IsAdminUser]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductFilter
    ordering_fields = ['title', 'price']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return []

# 4. Создание отзывов, доступно только залогиненным пользователям
# class CreateReview(CreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_serializer_context(self):
#         return {'request': self.request}


class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthorOrAdminPermission()]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update']:
            return [IsAdminUser()]
        else:
            return [DenyAll()]

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return queryset

# 5. Листинг отзывов (внутри деталей продукта) доступен всем
# 6. Редактр и удаление отзыва может делать только автор
# 7. Заказ может создать любой залогиненый пользователь
# 8. Список заказов: пользователь может видит только свои заказы, админы видят все
# 9. редактр заказы может только админ

#TODO: фильтрация по заказам
#TODO: Тесты
#TODO: документация
