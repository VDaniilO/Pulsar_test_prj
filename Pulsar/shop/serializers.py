from rest_framework import serializers
from .models import *


class ProductsSerializers(serializers.ModelSerializer):
    status = serializers.StringRelatedField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductsModel
        fields = ['title', 'article', 'price', 'status', 'image']

    @staticmethod
    def get_image(instance):
        all_form = ['jpg', 'webp', 'png']
        full_path = str(instance.path).split('.')
        img = {'path': full_path[0],
               'formats': [x for x in all_form if x != full_path[1]]}
        return img
