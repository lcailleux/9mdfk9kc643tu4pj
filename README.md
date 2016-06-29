## Truckfly Backend Interview

Your goal is to add new API endpoints to this app.

- `/fetch/`: when you POST to this endpoint, the app should fetch the last 10 truck gifs from the [Giphy API](https://github.com/Giphy/GiphyAPI) and store their URL, title, dimensions to the database
- `/gifs/`: list the available gifs from the database
- `/gifs/<gif_id>/`: add, get details, delete, or update a single gif
- `/gifs/random/`: should return one single random gif from the database

Only an authenticated user should have access to these endpoints. Only a superuser should be able to delete an image.

[:truck: Happy coding! :truck:](http://media1.giphy.com/media/2G4flVpbo6RmE/giphy.gif)
