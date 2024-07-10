import cv2
import numpy as np  

def callback(x):
    pass

#cap = cv2.VideoCapture(0)
global imagem
imagem = cv2.imread('../src/lula.jpeg')

img = imagem.copy()

def callback(x):
    pass

cv2.namedWindow('image')

#cascade methods for face and eyes

face_cascade_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# create trackbars

cv2.createTrackbar('scaleFactor_trackbar','image',110,300,callback)
cv2.createTrackbar('minNeighbors_trackbar','image',26,40,callback)

imagem_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade_classifier.detectMultiScale(imagem_cinza,scaleFactor=1.1, minNeighbors=6)
eyes = eye_cascade_classifier.detectMultiScale(imagem_cinza)

while True:

    img = imagem.copy()

    # get trackbar positions
    scaleFactor_cv = cv2.getTrackbarPos('scaleFactor_trackbar', 'image')
    minNeighbors_cv = cv2.getTrackbarPos('minNeighbors_trackbar', 'image')
    
    for (x,y,w,h) in faces:
    
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = imagem_cinza[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade_classifier.detectMultiScale(roi_color, scaleFactor=(int(scaleFactor_cv)/100), minNeighbors=int(minNeighbors_cv))

        print("Found {0} eyes!".format(len(eyes)))        
        
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
    cv2.imshow('image', img)
 
    k = cv2.waitKey(1000) & 0xFF # large wait time to remove freezing
    if k == 113 or k == 27:
        break