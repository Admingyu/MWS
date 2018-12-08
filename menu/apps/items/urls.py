from django.conf.urls import url

from items import views

urlpatterns = [
    url('', views.ItemsView.as_view()),
    url('/all', views.ItemsView),
    url('/(?P<pk>\d+)/$', views.ViewSetView.as_view({'get': 'retrieve'})),
    url('/ItemAPIView', views.ItemAPIView),
    url('/ItemGenericAPIView', views.ItemGenericAPIView),
]
