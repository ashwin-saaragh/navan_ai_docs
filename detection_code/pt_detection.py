import torch
import cv2
from PIL import Image
import os
import argparse
import random

# get path to the downloaded model and image to predict as arguments 
parser = argparse.ArgumentParser(description='Argument to collect info')
parser.add_argument('--model_path', help='path to the downloaded model')
parser.add_argument('--image_path', help='path to the test image')


args = parser.parse_args()
model_path = args.model_path
img_path = args.image_path

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = torch.hub.load("WongKinYiu/yolov7","custom",f"{model_path}",trust_repo=True)

img = cv2.imread(img_path)

results = model(img)
print(results.pandas().xyxy)
df = results.pandas().xyxy[0]

for _,row in df.iterrows():
    text = f"{row['name']}:{row['confidence']:.2f}"
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.75, 2)[0][1]
    cv2.rectangle(img,(int(row['xmin']), int(row['ymin'])),(int(row['xmax']), int(row['ymax'])), [random.randint(0, 255) for _ in range(3)], 2)
    cv2.putText(img,text,(int(row['xmin']), int(row['ymin']) + text_size),cv2.FONT_HERSHEY_SIMPLEX,0.75,(255,155,0),thickness=2)
     
Image.fromarray(img).save(f"out_{img_path.split(os.sep)[-1]}")
