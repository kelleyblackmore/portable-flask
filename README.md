## DOCKER with python flask app



### Build the app

docker build -t py_flask .

docker run -p 8080:8080 docker.pkg.github.com/kelleyblackmore/portable-flask/portableflask:latest


#### run detached
docker run -d -p 8080:8080 docker.pkg.github.com/kelleyblackmore/portable-flask/portableflask:latest
