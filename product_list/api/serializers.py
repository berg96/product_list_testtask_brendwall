from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    price = serializers.IntegerField(min_value=1)

    class Meta:
        model = Product
        fields = '__all__'
