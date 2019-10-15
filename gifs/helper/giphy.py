import requests
import dbsettings


class GiphyConfiguration(dbsettings.Group):
    api_key = dbsettings.StringValue()
    search_endpoint = dbsettings.StringValue()
    search_limit = dbsettings.PositiveIntegerValue()
    search_offset = dbsettings.PositiveIntegerValue()


class Giphy:
    configuration = GiphyConfiguration('Giphy Configuration')
    url = "https://api.giphy.com/"
    api_key = "KfJPspxkcEG1cQq1sQWkRzXHg3cZIs2m"

    def __init__(self):
        self.validate_configuration()

    def getTruckGifs(self):
        url = self.getUrl('v1/gifs/search?q=truck', "KfJPspxkcEG1cQq1sQWkRzXHg3cZIs2m")
        response = requests.get(url).json()

        if response['data']:
            return response['data']

    def getUrl(self, path, api_key):
        url = self.url
        url += path
        url += '&apikey=' + api_key + '&limit=10&offset=0&lang=en'
        return url

    def validate_configuration(self):
        for configuration in self.configuration:
            key, value = configuration
            if not value:
                raise IndexError(
                    "Giphy configuration field '{0}' not set. Did you set the configuration in admin/settings?"
                    .format(key)
                )
        return True




