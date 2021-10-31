from rest_framework import serializers
from order.models import Shop, Menu, Order, Orderfood

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        # 일부설정은 아래처럼
        # fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'