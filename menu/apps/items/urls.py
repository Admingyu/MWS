from django.conf.urls import url

from items import views

urlpatterns = [
    url('itemView$', views.ItemsView.as_view()),
    url('all', views.ItemsView),
    url('(?P<pk>\d+)/$', views.ViewSetView.as_view({'get': 'retrieve', 'post': 'update'})),
    url('ItemAPIView', views.ItemAPIView),
    url('ItemGenericAPIView', views.ItemGenericAPIView),
]
