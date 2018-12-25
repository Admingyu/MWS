from django.conf.urls import url

from others import views

urlpatterns = [
    url('', views.AddRecord.as_view())

]
