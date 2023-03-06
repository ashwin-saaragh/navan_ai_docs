import requests

url = "http://54.164.153.6:5001/predict?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoiMTYzNzk2NTY0NCIsInByb2plY3RfaWQiOiIxNTIzMDMxMTIyIiwiZWZmbmV0X21vZGVsX25hbWUiOiJlZmZpY2llbnRuZXR2Mi1iMCJ9.SoBQvzRsECngpQpwO3sNbmLgO85aJzffBn6ymvfY0fo"

payload={}
files=[
  ('up_img',('Joey-bloope-reel-599507.jpg',open('/C:/Users/AsH23/Downloads/Joey-bloope-reel-599507.jpg','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)