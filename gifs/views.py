from gifs.helper.giphy import Giphy
from gifs.models import Gif
from gifs.serializers import GifSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class GifViewSet(viewsets.ModelViewSet):
    queryset = Gif.objects.all()
    serializer_class = GifSerializer

    def list(self, request, *args, **kwargs):
        """
        GET /gifs
        """
        queryset = Gif.objects.all()
        serializer = GifSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def fetch(self, request):
        """
        POST /gifs/fetch
        """
        connector = Giphy()
        gif_list = connector.getGifs()

        i = 0
        response = {"result": True, "errors": []}
        for gif in gif_list:
            try:
                Gif.objects.update_or_create(
                    url=gif['url'],
                    defaults={
                        "title": gif['title'],
                        "width": gif['images']['original']['width'],
                        "height": gif['images']['original']['height']
                    }
                )
                i = i + 1
            except KeyError as error:
                response['errors'].append(str(error) + ": is nor defined")
                continue
        response["message"] = "{0} values imported".format(i)
        return Response(response)

    @action(methods=['get'], detail=False)
    def stats(self, request):
        """
        GET /gifs/stats
        """
        gif = Gif()

        count = gif.count()
        avg_width = gif.average('width')
        avg_height = gif.average('height')
        percentile_width = gif.percentile('width')
        percentile_height = gif.percentile('height')

        titles = gif.common_words('title')

        response = {
            "count": count,
            "average": {
                "height": avg_height,
                "width": avg_width
            },
            "90th": {
                "height": percentile_height,
                "width": percentile_width
            },
            "common_words_title": [titles]
        }

        return Response(response)

