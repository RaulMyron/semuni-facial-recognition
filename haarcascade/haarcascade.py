import cv2
import numpy as np
import matplotlib.pyplot as plt

#img = cv2.imread('../src/tyler.jpg') tyler
#img = cv2.imread('../src/sk.jpg')
#img = cv2.imread('../src/cage.webp')
img = cv2.imread('../src/bey.webp')

imagem_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# metodo um de chamar o metodo
face_cascade_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

#extrai a pose das faces

faces = face_cascade_classifier.detectMultiScale(imagem_cinza,scaleFactor=1.3, minNeighbors=5)
eyes = eye_cascade_classifier.detectMultiScale(imagem_cinza)

#x, y, largura e altura

#bota um quadrado
for(x,y,l,a) in faces:
    cv2.rectangle(img, (x,y), (x+l, y+a), (0,255,0))

'''for(x,y,l,a) in eyes:
    cv2.rectangle(img, (x,y), (x+l, y+a), (0,255,0))    
  '''  
for (x,y,w,h) in faces:
    
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = imagem_cinza[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    #eyes = eye_cascade_classifier.detectMultiScale(roi_color, scaleFactor=1.5, minNeighbors=26) tyler
    #eyes2 = eye_cascade_classifier.detectMultiScale(roi_color, scaleFactor=1.1, minNeighbors=6) sk
    
    #eyes = eye_cascade_classifier.detectMultiScale(roi_color, scaleFactor=1.5, minNeighbors=14) bey
    
    print("Found {0} eyes!".format(len(eyes)))        
    
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    try:
        for (ex,ey,ew,eh) in eyes2:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    except: 
        pass

    for (x,y,w,h) in faces:
    
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = imagem_cinza[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        #eyes = eye_cascade_classifier.detectMultiScale(roi_color, scaleFactor=1.5, minNeighbors=26) tyler
        #eyes2 = eye_cascade_classifier.detectMultiScale(roi_color, scaleFactor=1.1, minNeighbors=6) sk
        
        eyes = eye_cascade_classifier.detectMultiScale(roi_color, scaleFactor=1.5, minNeighbors=14) #bey
        
        print("Found {0} eyes!".format(len(eyes)))        
        
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        try:
            for (ex,ey,ew,eh) in eyes2:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        except: 
            pass

cv2.imshow("w", img)

cv2.waitKey(0)