from django.contrib import admin
from .models import ProductsModel, ProductStatusModel


admin.site.register(ProductsModel)
admin.site.register(ProductStatusModel)
