# Testing Model deployment with API

## How to hit the API endpoint once deployed in Navan server:

- Once you click the deploy button and service is deployed you will get a token unique to your model and also a cURL sample

                curl --location 'http://54.164.153.6:5001/predict?token=<your token>' \
                --form 'up_img=@<filepath to image>'
- Please store token securely and pass it along with filepath to image to predict to the api
- You can checkout the document for the api by visiting the link in your browser : [http://54.225.11.253:5001/docs](http://54.225.11.253:5001/docs)
- API returns the predicted class and the probability for each class in the model

        {
                "prediction": "Class_1",
                "prediction_probability": 
                {
                        "Class_1": "0.58513",
                        "Class_2": "0.41486"
                }
        }
- We have sample scripts for your reference 

  - [Sample Python Script](https://github.com/saaragh/navan_ai_docs/blob/main/deploy_model_as_api/sample.py) 
  - [Sample JS script](https://github.com/saaragh/navan_ai_docs/blob/main/deploy_model_as_api/sample.js)