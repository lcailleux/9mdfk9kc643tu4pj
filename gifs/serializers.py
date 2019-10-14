from gifs.models import Gif

from rest_framework import serializers


class GifSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gif
        fields = ['id', 'title', 'url', 'width', 'height']

