"""
Продукты могут фильтроваться по категории, по названию , по цене (дороже, дешевле)

Заказы могут фильтроваца (по продукту , по дате, по сумме)
"""
import django_filters
from django_filters.rest_framework import FilterSet

from main.models import *


class ProductFilter(FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
    price_from = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price_from', 'price_to')


class OrderFilter(FilterSet):
    """фильтрация по сумме(от, до)
    по  товару, по статусу, по дате"""
    total_sum_from = django_filters.NumberFilter(field_name='total_sum', lookup_expr='gte')
    total_sum_to = django_filters.NumberFilter(field_name='total_sum', lookup_expr='lte')
    created_at = django_filters.DateTimeFromToRangeFilter(field_name='created_at')
    product = django_filters.CharFilter(field_name='products__product__title', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ('total_sum_from', 'total_sum_to', 'created_at', 'product')