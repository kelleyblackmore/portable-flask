## DOCKER with python flask app

This code was taken from docker.com


### Build the app


docker build -t py_flask .


docker run -p 4000:80 py_flask


#### run detached
docker run -d -p 4000:80 py_flask