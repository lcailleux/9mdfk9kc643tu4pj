from gifs.helper.giphy import Giphy
from gifs.models import Gif
from gifs.serializers import GifSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class GifViewSet(viewsets.ModelViewSet):
    queryset = Gif.objects.all()
    serializer_class = GifSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def list(self, request, *args, **kwargs):
        """
        GET /gifs
        """
        queryset = Gif.objects.all()
        serializer = GifSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        DELETE /gifs/<gif_id>/
        """
        if request.user.is_superuser:
            return super().destroy(self, request, args, kwargs)
        return Response(data={"detail": "You do not have the permission to remove this."}, status=403)

    @action(methods=['post'], detail=False)
    def fetch(self, request):
        """
        POST /gifs/fetch
        """

        try:
            connector = Giphy()
            gif_list = connector.getTruckGifs()
        except IndexError as error:
            return Response({'detail': error.__str__()})

        i = 0
        response = {"detail": []}
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
                response['detail'].append(str(error) + ": is nor defined")
                continue
        response["detail"] = "{0} values imported".format(i)
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
                "height": round(avg_height, 2),
                "width": round(avg_width, 2)
            },
            "90th": {
                "height": round(percentile_height, 2),
                "width": round(percentile_width, 2)
            },
            "common_words_title": [titles]
        }
        return Response(response)

