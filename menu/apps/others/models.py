from django.db import models

# Create your models here.
from menu.utils.base_model import BaseModel


class WxHead(BaseModel):
    user = models.CharField(max_length=20, verbose_name='微信昵称')
    phonoe = models.CharField(max_length=20, verbose_name='手机型号')
    head_image = models.ImageField(verbose_name="头像")

    class Meta:
        db_table = "db_others"
        verbose_name = "微信用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user
