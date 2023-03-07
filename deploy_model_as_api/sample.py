import requests

url = "https://inference.navan.ai/predict?token=<your token>"

payload={}
files=[
  ('file',('<image file name>',open('<path to image file>','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)