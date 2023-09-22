import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)

while True:

    _, video_frame = video_capture.read()  # read frames from the video
    
    gray_image = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(gray_image, 1.5, 6, minSize=(40, 40))
    
    print(faces)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(video_frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

    cv2.imshow(
        "My Face Detection Project", video_frame
    )  # display the processed frame in a window named "My Face Detection Project"

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
