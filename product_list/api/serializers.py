from rest_framework import serializers

from products.models import Product


NEGATIVE_PRICE = 'Цена должна быть больше нуля.'


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    price = serializers.IntegerField(min_value=1)

    class Meta:
        model = Product
        fields = '__all__'
