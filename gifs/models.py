from django.db import models
import numpy as np
from collections import Counter


class Gif(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    url = models.TextField(unique=True)
    width = models.IntegerField()
    height = models.IntegerField()

    def count(self):
        return Gif.objects.all().count()

    def average(self, field):
        average_data = Gif.objects.all().aggregate(models.Avg(field))
        try:
            average_value = average_data[field + "__avg"]
        except KeyError:
            average_value = 0
        return average_value

    def percentile(self, field, percentile=90):
        values = Gif.objects.values_list(field, flat=True)
        return np.percentile(values, percentile)

    def common_words(selfs, field):
        values = Gif.objects.values_list(field, flat=True)
        values = [words for segments in values for words in segments.split()]
        most_common_values = Counter(values).most_common(10)
        common_words = []
        for key, value in most_common_values:
            common_words.append({"word": key, "count": value})
        return common_words
