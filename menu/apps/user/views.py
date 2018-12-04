import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


from user.models import User
from user.serializers import UserSerializer


class HomeView(View):

    def get(self, request):
        queryset = User.objects.all()
        # serializer_class = UserSerializer

        user_list = []
        for user in queryset:
            user_list.append({
                'username': user.username,
                'email': user.email,
                'mobile': user.mobile,
            })

        return JsonResponse(user_list, safe=False)



