from django.contrib import admin
from gifs.models import Gif


class GiphyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'width', 'height')
    pass


admin.site.register(Gif, GiphyAdmin)
