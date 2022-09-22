# Testing with Docker Image 

## How to run the docker image you've downloaded:

Docker images are built with a copy of the model you've generated. The image will be tar file with the model_name*** as name, please follow the steps on how to load the docker image and run image prediction

- First step is to load the image in your local docker setup. Go to the directory where the model file is downloaded, open a terminal and run the following command.

        docker load -i {model_name***}.tar
- Once loaded you can check the using the following command, and you will see an image with your model name in the list of repositories.
        
        docker images
- Now you can start a container with the image you've downloaded using the following command. You need to pass the port_no which is available/not used by another process in your system.

        docker run -e port_no={port_no} -it -p {port_no}:{port_no} {model_name***}
- Once started, wait till you see **'Application startup complete'** msg in the logs. 
- Now you've container running and you can checkout the document for the api by visiting the link in your browser : **localhost:{port_no}/docs**
- Alternatively you can try to hit the api endpoint using the following curl as reference

        curl -X 'POST' 'http://localhost:{port_no}/upload' -H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'file=@{img}.jpg;type=image/jpeg'
