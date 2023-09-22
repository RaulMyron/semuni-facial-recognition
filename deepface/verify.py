from deepface import DeepFace
import matplotlib.pyplot as plt 
import cv2
import numpy as np

result = DeepFace.verify(img1_path = "../src/rau4.jpg", img2_path = "../src/rau5.jpg", enforce_detection=False)
result2 = DeepFace.verify(img1_path = "../src/bey.webp", img2_path = "../src/tyler.jpg")
result3 = DeepFace.verify(img1_path = "../src/tyler.jpg", img2_path = "../src/tyler.jpg")
result4 = DeepFace.verify(img1_path = "../src/tyler3.webp", img2_path = "../src/tyler.jpg")
result5 = DeepFace.verify(img1_path = "../src/bey.webp", img2_path = "../src/tyler.jpg")

#print(result)
print(result5)