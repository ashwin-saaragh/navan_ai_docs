# Testing Model deployment with API

## How to hit the API endpoint once deployed in Navan server:

- Once you click the deploy button and service is deployed you will get the endpoint like this

                http://3.229.179.40/{port_no}
- You can checkout the document for the api by visiting the link in your browser : 

                http://3.229.179.40/:{port_no}/docs
- Alternatively you can try to hit the api endpoint using the following curl as reference

        curl -X 'POST' 'http://3.229.179.40/:{port_no}/upload' -H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'file=@{img}.jpg;type=image/jpeg'