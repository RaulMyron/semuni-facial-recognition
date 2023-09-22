from deepface import DeepFace
import matplotlib.pyplot as plt 
import cv2
import numpy as np

backends = ["opencv", "ssd", "dlib", "mtcnn", "retinaface", "mediapipe"]

img = cv2.imread('../src/tyler.jpg')

face = DeepFace.extract_faces("../src/tyler.jpg", target_size=(224,224), detector_backend="opencv")

print(face[0]["facial_area"])

x, y, a, l = face[0]["facial_area"]["x"], face[0]["facial_area"]["y"], face[0]["facial_area"]["w"], face[0]["facial_area"]["h"]

cv2.rectangle(img,(x,y),(x+a,y+a),(0,255,0),2)

result = DeepFace.verify(img1_path = "../src/rau2.jpg", img2_path = "../src/rau3.jpg", enforce_detection=False)

print(result)

cv2.imshow("oi",img)
cv2.waitKey(0)