import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from items.models import Item
from items.serializers import ItemSerializer


# View
class ItemsView(View):

    def get(self, request):
        queryset = Item.objects.all()
        item_list = []
        for item in queryset:
            item_list.append({
                'id': item.id,
                'name': item.name,
                'price': item.price,
                'descr': item.descr,
                'create_time': item.create_time,
                'update_time': item.update_time
            })
        return JsonResponse(item_list, safe=False, status=200)

    def post(self, request):
        try:
            json_bytes = request.body
            json_str = json_bytes.decode()
            item_dic = json.loads(json_str)
            print(item_dic)
        except BaseException as e:
            print(e)
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST, data={'errmsg': '传递参数格式错误'})

        try:
            item = Item.objects.create(
                name=item_dic.get('name'),
                price=item_dic.get('price'),
                descr=item_dic.get('descr'),
            )
        except BaseException as e:
            print(e)
            return JsonResponse(errmsg='参数不完整', status=status.HTTP_400_BAD_REQUEST, data={'errmsg': '传递参数格式错误'})

        return JsonResponse(item_dic, safe=False)


# APIView
class ItemAPIView(APIView):
    queryset = Item
    serializer_class = ItemSerializer

    def get(self, request):
        items = Item.objects.all()
        serialized = ItemSerializer(instance=items)

        return Response(serialized.data, status=200)


# GenericAPIView
class ItemGenericAPIView(GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)


# ListModelMixin
class ListModelMixinView(ListModelMixin, GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request):
        return self.list(request)


# CreateModelMixin
# class CreateModelMixinView(CreateModelMixin, GenericAPIView):


# viewsets.ViewSet
class ViewSetView(viewsets.ViewSet):

    def list(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            item = Item.objects.get(id=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ItemSerializer(item)

        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Item.objects.get(id=pk)
            print(item)
            item.name = request.data.get('name')
            item.save()
        except Item.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = ItemSerializer(item)

        return Response(serialized.data)
