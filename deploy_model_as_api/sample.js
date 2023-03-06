var formdata = new FormData();
formdata.append("up_img", fileInput.files[0], "/C:/Users/AsH23/Downloads/Joey-bloope-reel-599507.jpg");

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("http://54.164.153.6:5001/predict?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoiMTYzNzk2NTY0NCIsInByb2plY3RfaWQiOiIxNTIzMDMxMTIyIiwiZWZmbmV0X21vZGVsX25hbWUiOiJlZmZpY2llbnRuZXR2Mi1iMCJ9.SoBQvzRsECngpQpwO3sNbmLgO85aJzffBn6ymvfY0fo", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));