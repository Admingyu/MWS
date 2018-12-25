from django.utils import timezone
from rest_framework import serializers

from others.models import WxHead


class WxHeadSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    phonoe = serializers.CharField(max_length=20, label="手机号")
    head_image = serializers.ImageField(label="头像")
    create_time = serializers.DateTimeField(label='发布日期', required=False, read_only=True)
    update_time = serializers.DateTimeField(label='更新日期', required=False, default=timezone.now())

    class Meta:
        model = WxHead
        fields = "__all__"


