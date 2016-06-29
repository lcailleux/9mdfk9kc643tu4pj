## Truckfly Backend Interview

Your goal is to add new API endpoints to this app.

- `/fetch/`: when you POST to this endpoint, the app should fetch the last 10 truck photos from the Flickr API and store their URL, title, dimensions to the database
- `/photos/`: list the available photos from the database
- `/photos/<photo_id>/`: add, get details, delete, or update a single photo
- `/photos/random/`: should return one single random photo from the database

Only an authenticated user should have access to these endpoints. Only a superuser should be able to delete an image.

:truck: Happy coding! :truck:
