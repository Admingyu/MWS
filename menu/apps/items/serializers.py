import datetime

from django.utils import timezone
from rest_framework import serializers

from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='名称', max_length=20)
    price = serializers.DecimalField(label='价格', max_digits=8, decimal_places=2)  # decimal_places指小数点后面有几位
    descr = serializers.CharField(label='描述', max_length=24)
    create_time = serializers.DateTimeField(label='发布日期', required=False, read_only=True)
    update_time = serializers.DateTimeField(label='更新日期', required=False, default=timezone.now())

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.name
        instance.price = validated_data.price
        instance.descr = validated_data.descr
        instance.update_time = validated_data.update_time

    class Meta:
        model = Item
        fields = '__all__'
