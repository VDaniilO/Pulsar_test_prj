import rest_framework.filters
from django_filters import rest_framework
from .models import ProductsModel


class MoreFiltersProd(rest_framework.BaseInFilter, rest_framework.CharFilter):
    pass


class ProductsFilter(rest_framework.Filter):
    article = MoreFiltersProd(field_name='article', lookup_expr='in')
    title = MoreFiltersProd(field_name='title', lookup_expr='in')

    class Meta:
        model = ProductsModel
        fields = ['article', 'title']
