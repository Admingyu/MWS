import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from items.models import Item
from items.serializers import ItemSerializer


class ItemsView(View):

    def get(self, request):
        queryset = Item.objects.all()
        item_list = []
        for item in queryset:
            item_list.append({
                'id': item.id,
                'name': item.name,
                'price': item.price,
                'descr': item.descr
            })
        return JsonResponse(item_list, safe=False, status=200)

    def post(self, request):
        json_bytes = request.body
        json_str = json_bytes.decode()
        item_dic = json.loads(json_str)
        print(item_dic)
        item = Item.objects.create(
            name=item_dic.get('name'),
            price=item_dic.get('price'),
            descr=item_dic.get('descr'),
        )

        return JsonResponse(item_dic)


class ItemViewSet(ModelViewSet):
    queryset = Item
    serializer_class = ItemSerializer
