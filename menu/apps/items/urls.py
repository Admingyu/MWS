from django.conf.urls import url

from items import views

urlpatterns = [
    url('', views.ItemsView.as_view()),
    url('/all', views.ItemsView)
]
