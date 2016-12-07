# truckfinder URL Configuration

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from truckfinder.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
