import requests
import dbsettings


class GiphyConfiguration(dbsettings.Group):
    api_key = dbsettings.StringValue()
    search_endpoint = dbsettings.StringValue(default="http://api.giphy.com/v1/gifs/search")


class Giphy:
    configuration = GiphyConfiguration('Giphy Configuration')

    def __init__(self):
        self.validate_configuration()

    def getTruckGifs(self):
        url = self.getSearchUrl('trucks')
        response = requests.get(url).json()

        if response['data']:
            return response['data']

    def getSearchUrl(self, query, search_offset='0', search_limit='10'):
        return self.configuration.search_endpoint + '?q=' + query \
               + '&apikey=' + self.configuration.api_key \
               + '&offset=' + search_offset \
               + '&limit=' + search_limit

    def validate_configuration(self):
        for configuration in self.configuration:
            key, value = configuration
            if not value:
                raise IndexError(
                    "Giphy configuration field '{0}' not set. Did you set the configuration in admin/settings?"
                    .format(key)
                )
        return True




