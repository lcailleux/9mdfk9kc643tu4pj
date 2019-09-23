## Dashdoc Backend Interview

Your goal is to add new API endpoints to this app. 
You can also create a new app from scratch if you're not familiar with Python.

- POST `/gifs/fetch/`: when you POST to this endpoint, the app should fetch the last 10 truck gifs from the [Giphy API](https://developers.giphy.com/docs/api/endpoint#search) and store their URL, title, dimensions to the database
- GET `/gifs/`: list the available gifs from the database
- POST/GET/DELETE/PATCH `/gifs/<gif_id>/`: add, get details, delete, or update a single gif
- GET `/gifs/stats/`: return stats about the gifs stored in DB, in this shape:
```
{
   "count": 10, // total number of gifs in db
   "average": { // values averaged over all gifs
       "height": 203.3,
       "width": 330.12
   },
   "90th": { // 90th-percentile values over all gifs
       "height": 289.39,
       "width": 420.94,
   },
   "common_words_title": [ // list the top 10 words in the title of the gifs, lowercased and sorted by most common first
       {"word": "truck", "count": 8},
       {"word": "happy", "count": 3},
       ...
   ]
}
```

Only an authenticated user should have access to these endpoints. Only a superuser should be able to delete an image.

[:truck: Happy coding! :truck:](http://media1.giphy.com/media/2G4flVpbo6RmE/giphy.gif)
