references

> https://docs.opencv.org/3.1.0/d7/d8b/tutorial_py_face_detection.html#gsc.tab=0
> https://www.youtube.com/watch?v=F7uw3oPC1wQ&list=PLsyobOqUhkthjvmA_s7tTjb7V2EiwYYGC&index=2
> https://www.geeksforgeeks.org/python-haar-cascades-for-object-detection/
> 

Amongst these parameters, you need to pay more attention to four of them:

scaleFactor – Parameter specifying how much the image size is reduced at each image scale.
Basically, the scale factor is used to create your scale pyramid. More explanation, your model has a fixed size defined during training, which is visible in the XML. This means that this size of the face is detected in the image if present. However, by rescaling the input image, you can resize a larger face to a smaller one, making it detectable by the algorithm. 1.05 is a good possible value for this, which means you use a small step for resizing, i.e. reduce the size by 5%, you increase the chance of a matching size with the model for detection is found. This also means that the algorithm works slower since it is more thorough. You may increase it to as much as 1.4 for faster detection, with the risk of missing some faces altogether.

minNeighbors – Parameter specifying how many neighbors each candidate rectangle should have to retain it.
This parameter will affect the quality of the detected faces. Higher value results in fewer detections but with higher quality. 3~6 is a good value for it.

minSize – Minimum possible object size. Objects smaller than that are ignored.
This parameter determines how small size you want to detect. You decide it! Usually, [30, 30] is a good start for face detection.

maxSize – Maximum possible object size. Objects bigger than this are ignored.
This parameter determines how big size you want to detect. Again, you decide it! Usually, you don't need to set it manually, the default value assumes you want to detect without an upper limit on the size of the face.