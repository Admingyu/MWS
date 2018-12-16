# Create your models here.
from django.db import models
from django.utils import timezone

from menu.utils.base_model import BaseModel


class Item(BaseModel):
    name = models.CharField(max_length=20, verbose_name='名称')
    price = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='单价')
    descr = models.CharField(max_length=24, verbose_name='描述')
    create_time = models.DateTimeField(auto_now=True, verbose_name='发布日期')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='更新日期')

    class Meta:
        db_table = 'tb_item'
        verbose_name = '项目'
        verbose_name_plural = verbose_name

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
