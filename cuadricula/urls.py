from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'albums', views.AlbumViewSet)


urlpatterns = [
    url('^api/', include(router.urls)),
    url('', views.index, name='albums')
]