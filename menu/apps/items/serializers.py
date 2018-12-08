from rest_framework import serializers

from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='名称', max_length=20)
    price = serializers.DecimalField(label='价格', max_digits=8, decimal_places=4)
    descr = serializers.CharField(label='描述', max_length=24)
    create_time = serializers.DateField(label='发布日期', required=False)
    update_time = serializers.DateField(label='发布日期', required=False)

    def create(self, validated_data):
        return Item.objects.create(**validated_data)
    # class Meta:
    #     models = Item
    #     fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.name
        instance.price = validated_data.price
        instance.descr = validated_data.price
        instance.update_time = validated_data.update_time

