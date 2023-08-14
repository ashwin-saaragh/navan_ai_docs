# Testing with Docker Image 

## How to run the docker image you've downloaded:
- Once you click Download button you will get three files.
  1. A Docker image file in .tar format &rarr; base_img.tar
  2. Model file in .pt format &rarr; best.pt
  3. A file with list of classes &rarr; classes.names   

- Docker image has the all prerequisite installed. First step is to load the image in your local docker setup. Go to the directory where the model file is downloaded, open a terminal and run the following command.

        docker load -i base_img.tar
- Once loaded you can check the local docker images using the following command, and you will see an image named base_img in the list of repositories.
        
        docker images
- Now you can start a container with the image you've downloaded using the following command. 
  1. You need to mount the {path/to/download_dir} to the running container(you can copy the 3 downloaded files to a directory and mount that path). 
  2. pass the port_no which is available/not used by another process in your system. 

         docker run -v {path/to/download_dir}:/usr/src/app/models/v1.0/ -it -p {port_no}:{port_no} base_img python app.py --port_no {port_no}
- Once started, wait till you see **'Application startup complete'** msg in the logs. 
- Now you've container running and you can checkout the document for the api by visiting the link in your browser : **localhost:{port_no}/docs**
- Alternatively you can try to hit the api endpoint using the following curl as reference

        curl -X 'POST' 'http://localhost:{port_no}/inference' -H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'file=@{img}.jpg;type=image/jpeg'
