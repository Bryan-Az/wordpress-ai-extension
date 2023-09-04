The goal for this project is to deploy a machine learning model that is hosted on a live wordpress website, by launching a docker-compose stack.

The overview of the model is available to view on medium, here: https://medium.com/@bryanambzam/a-detection-algorithm-using-scikit-learn-chat-gpt-4-to-identify-images-of-kangaroos-8d3aae90dcb6

docker-compose.yml: This file will define the services that make up the application in docker so they can be run together in an isolated environment.

Dockerfile: This file will define the environment in which our Python script will run.

requirements.txt: This file will list the Python dependencies that need to be installed in the Docker container.

app.py: This is the main Python script that will load the model, connect to the MySQL database, handle image uploads, and return the score.

kangaroo_classifier_model.pki: This is the pre-trained machine learning model that will be used to predict the score.

wordpress_plugin.php: This is the WordPress plugin that will create the front-end interface for users to upload images and view the score.
