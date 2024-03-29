# truckfinder URL Configuration

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from truckfinder.views import UserViewSet
from gifs.views import GifViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'gifs', GifViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/settings/', include('dbsettings.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
