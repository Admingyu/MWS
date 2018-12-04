from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from items.models import Item


class User(AbstractUser):

    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号', null=True)
