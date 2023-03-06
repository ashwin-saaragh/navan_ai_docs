var formdata = new FormData();
formdata.append("file", fileInput.files[0], "<path to image file>");

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("http://54.164.153.6:5001/predict?token=<your token>", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));