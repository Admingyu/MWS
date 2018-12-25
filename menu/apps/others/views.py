from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from requests import Response

from others.models import WxHead


class AddRecord(View):
    def post(self, request):
        new_record = WxHead()
        new_record.user = request.form.get("user")
        new_record.head_image = request.form.get("phonoe")

        new_record.save()
        return JsonResponse(status=200, data={"status": "ok"})
