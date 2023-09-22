


```bash

git clone https://github.com/AlexeyAB/darknet

cd darknet

make

wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights #tiny weights

/darknet detect <arquivo config> <arquivo dos pesos> <imagem> #example
/darknet detect cfg/yolov4.cfg yolov4.weights data/person.jpg #example

pip install opencv-contrib-python

```
> https://iaexpert.academy/2020/10/13/deteccao-de-objetos-com-yolo-uma-abordagem-moderna/?doing_wp_cron=1695119117.6073489189147949218750
