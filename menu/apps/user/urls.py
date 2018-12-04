from django.conf.urls import url

from user import views

urlpatterns = [

    url('', views.HomeView.as_view())

]
