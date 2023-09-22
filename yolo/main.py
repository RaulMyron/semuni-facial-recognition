import cv2
import time
import numpy as np

Conf_threshold = 0.4
NMS_threshold = 0.4
COLORS = [(0, 255, 0), (0, 0, 255), (255, 0, 0),
          (255, 255, 0), (255, 0, 255), (0, 255, 255)]

class_name = []

yolo_v = "tiny4"
#yolo_v = "yolo4"
#yolo_v = "yolo7"

if yolo_v == "tiny4":

    with open('yoloData/names.txt', 'r') as f:
        class_name = [cname.strip() for cname in f.readlines()]
        
    net = cv2.dnn.readNet('yoloData/yolov4-tiny.weights', 'yoloData/yolov4-tiny.cfg')
    
elif yolo_v == "yolo4":

    with open('yoloData/names.txt', 'r') as f:
        class_name = [cname.strip() for cname in f.readlines()]


    net = cv2.dnn.readNet('yoloData/yolov4.weights', 'yoloData/yolov4.cfg')

#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
#net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

cap = cv2.VideoCapture('../src/output.avi')

starting_time = time.time()
frame_counter = 0

while True:
    
    ret, frame = cap.read(0)
    
    frame_counter += 1
    
    if ret == False:
        break
    
    classes, scores, boxes = model.detect(frame, Conf_threshold, NMS_threshold)
    
    for (classid, score, box) in zip(classes, scores, boxes):
        
        color = COLORS[int(classid) % len(COLORS)]
        
        print(type(class_name[classid]))
        print(type(score))
        
        label = "%s : %f" % (class_name[classid], score)
        
        cv2.rectangle(frame, box, color, 1)
        cv2.putText(frame, label, (box[0], box[1]-10),
                   cv2.FONT_HERSHEY_COMPLEX, 0.3, color, 1)
        
    endingTime = time.time() - starting_time
    fps = frame_counter/endingTime
    
    # print(fps)
    
    cv2.putText(frame, f'FPS: {fps}', (20, 50),
               cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()