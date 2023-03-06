import requests

url = "http://54.164.153.6:5001/predict?token=<your token>"

payload={}
files=[
  ('up_img',('<image file name>',open('<path to image file>','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)