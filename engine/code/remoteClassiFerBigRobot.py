import urllib
import cv2
import numpy as np 
import dlib
import sys



url = "http://192.168.0.14:8080/shot.jpg"
imgResp =  urllib.urlopen(url)

x=0
y=0

detector = dlib.simple_object_detector("./classificador_bigrobot.svm")
font=cv2.FONT_HERSHEY_SIMPLEX


def detect_BigRobot(frame):
		objetosdetectados = detector(frame, 1)
		for o in objetosdetectados:
			e, t, d, f = (int(o.left()), int(o.top()), int(o.right()), int(o.bottom()))
			cv2.rectangle(frame, (e, t), (d, f), (0, 0, 255), 2)
			cv2.putText(frame,"Big Robot", (e,t), cv2.FONT_HERSHEY_SIMPLEX, 1, 235)
		cv2.imshow("Detect Big Robot", frame)

def decode(url):
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    frame0 = img
    return frame0

while True:
    frame0 = decode(url)
    detect_BigRobot(frame0)
    if ord('q')==cv2.waitKey(10):
        exit(0)

video_capture.release()
cv2.destroyAllWindows()