The goal for this project is to deploy a machine learning model that is hosted on a live wordpress website, by launching a docker-compose stack.

To use this app plugin, you need to run the docker-compose script in the main outer folder, and then once the wordpress site is available on localhost in your browser, you can then install the wordpress and after you're in the admin dashboard, head to the plugin section & activate the kangaroo detector plugin. Once it's activated you can create a post or use any available post to add a short-code block on your page with the code: [kangaroo_detector]

Once you publish & save, the post/page will now be able to present a form with an upload link. You can upload a png or jpg image. The plugin will communicate with the flask python app.py and then return a score as a response back to the javascript and edit the html to present the score! 


The overview of the model is available to view on medium, here: https://medium.com/@bryanambzam/a-detection-algorithm-using-scikit-learn-chat-gpt-4-to-identify-images-of-kangaroos-8d3aae90dcb6

docker-compose.yml: This file will define the services that make up the application in docker so they can be run together in an isolated environment.

Dockerfile: This file will define the environment in which our Python script will run.

requirements.txt: This file will list the Python dependencies that need to be installed in the Docker container.

app.py: This is the main Python script that will load the model, connect to the MySQL database, handle image uploads, and return the score.

kangaroo_classifier_model.pki: This is the pre-trained machine learning model that will be used to predict the score.

wordpress_plugin.php: This is the WordPress plugin that will create the front-end interface for users to upload images and view the score.
