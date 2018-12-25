from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from rest_framework.viewsets import ModelViewSet

from others.models import WxHead


# class AddRecord(View):
#     def post(self, request):
#         new_record = WxHead()
#         new_record.user = request.data.get("user")
#         new_record.head_image = request.data.get("phonoe")
#
#         new_record.save()
#         return JsonResponse(status=200, data={"status": "ok"})
#
#     def get(self, request):
#         return
from others.serializers import WxHeadSerializer


class AddRecord(ModelViewSet):
    queryset = WxHead.objects.all()
    serializer_class = WxHeadSerializer
