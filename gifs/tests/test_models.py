from django.test import TestCase
from ..models import Gif
from types import *


class GifTest(TestCase):
    def setUp(self):
        Gif.objects.create(
            title='test1 gif title',
            url='test_url',
            width=200,
            height=200
        )

    def test_get_gif(self):
        gif = Gif.objects.get(url='test_url')
        self.assertEqual(gif.url, 'test_url')

    def test_count(self):
        gif = Gif.objects.get(url='test_url')
        self.assertIsInstance(gif.count(), int)

    def test_avg(self):
        gif = Gif.objects.get(url='test_url')
        self.assertIsInstance(gif.average('width'), float)
        self.assertIsInstance(gif.average('height'), float)

    def test_percentile(self):
        gif = Gif.objects.get(url='test_url')
        self.assertIsInstance(gif.percentile('width'), float)
        self.assertIsInstance(gif.percentile('height'), float)

    def test_common_words(self):
        gif = Gif.objects.get(url='test_url')
        self.assertIsInstance(gif.common_words('title'), list)