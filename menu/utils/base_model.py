from django.db import models


class BaseModel(models.Model):
    id = models.IntegerField(primary_key=True)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True