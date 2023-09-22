from deepface import DeepFace
import matplotlib.pyplot as plt 
import cv2
import numpy as np

backends = ["opencv", "ssd", "dlib", "mtcnn", "retinaface", "mediapipe"]

#img = cv2.imread('../src/tyler.jpg')
#img = cv2.imread('../src/tyler3.webp')
#img = cv2.imread('../src/rau5.jpg')
img = cv2.imread('../src/rau4.jpg')

face = DeepFace.analyze("../src/tyler.jpg", actions = ['age', 'gender', 'race', 'emotion'])

print(face)