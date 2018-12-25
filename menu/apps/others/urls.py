from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from others import views

urlpatterns = [
    # url('', views.AddRecord.as_view())
    #url('', views.AddRecord.as_view)

]
router = DefaultRouter()
# 可以处理视图的路由器
router.register(r'', views.AddRecord)
urlpatterns += router.urls
print(router.urls)
# 向路由器中注册视图集
#