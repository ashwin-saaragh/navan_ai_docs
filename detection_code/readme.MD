# How to load and use the model file :

- Once you've downloaded the model file you can test it in your local system with the code snippet. Please use the Github repo with sample code using the link provided in export model page, and download teh pt_detection.py and requirements.txt files. 
- You need to have python installed in your system. python 2.7+ and 3.4+ comes with pip and virtualenv along with installation. Create an environment and install the required packages.
- Run the following command to install requirements using pip

        python -m pip install -r requirements.txt
- If you're using conda use the following command to install requirements
        
        conda install --file requirements.txt
- Then run the following command and pass as arguments the path to the downloaded model file and image file you want to detect with the model 

        python pt_detection.py --model_path path/to/downloaded/model_file  --image_path path/to/image_file
-  Please note if you're using python3.4 or above, try replacing **python** to **python3** if you're facing error while running the above command
- Output file(eg.out_<img_file_name>) with bounding box on the detected object will be generated in the current working directory where the command was run.  
