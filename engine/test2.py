import cv2
import cv2 as cv
import numpy as np

#img = cv2.imread('opencv.png',0)
img = cv2.imread('bolaping.jpg',0)
img = cv2.equalizeHist(img)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

#circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,param1=50,param2=30,minRadius=0,maxRadius=25)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()