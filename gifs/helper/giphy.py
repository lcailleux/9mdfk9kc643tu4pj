import requests

class Giphy:
    url = "https://api.giphy.com/"
    api_key = "KfJPspxkcEG1cQq1sQWkRzXHg3cZIs2m"

    def getGifs(self):
        url = self.getUrl('v1/gifs/search?q=truck', "KfJPspxkcEG1cQq1sQWkRzXHg3cZIs2m")
        response = requests.get(url).json()

        if response['data']:
            return response['data']

    def getUrl(self, path, api_key):
        url = self.url
        url += path
        url += '&apikey=' + api_key + '&limit=10&offset=0&lang=en'
        return url




