from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time
from time import sleep 

class Camera:
   
    def __init__(self,detect_line,detect_color, detect_circle):
       self.detect_line = detect_line 
       self.detect_color = detect_color
       self.detect_circle = detect_circle
       #pass
    def Line(self): ## dar direcao ao robo
      if self.detect_line == 1:
         (grabbed, Frame) = camera.read()
         if (grabbed):
           dado = pre_processing(Frame)
           Direcao, Qtdlines = dado.TratarImagem()
           print "Direcao: " ,Direcao,"Quantidade de Linhas: ",Qtdlines
           return  Direcao,Qtdlines
  
    def cor(self):
    #""" Falta Implementar """
       pass 
   
    def circle(self):
       if self.detect_circle == 1:
         (grabbed, Frame) = camera.read()
         if (grabbed):
           dado = pre_processing(Frame)
           bola,centro = dado.TratarCircle()
           return bola,centro
     



#camera = cv2.VideoCapture(0)
#camera = cv2.VideoCapture("simulacao.mp4") # line
camera = cv2.VideoCapture("circulosimulation.mp4")
camera.set(3,320)
camera.set(4,240)
LimiarBinarizacao = 125       #este valor eh empirico. Ajuste-o conforme sua necessidade 
AreaContornoLimiteMin = 5000  #este valor eh empirico. Ajuste-o conforme sua necessidade 

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
 

   
class pre_processing:
   def __init__(self,img):
      self.img = img
    
   def TratarImagem(self):
      #obtencao das dimensoes da imagem
      height = np.size(self.img,0)
      width= np.size(self.img,1)
      QtdeContornos = 0
      DirecaoASerTomada = 0
    
      #tratamento da imagem
      gray = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
      gray = cv2.GaussianBlur(gray, (21, 21), 0)
      FrameBinarizado = cv2.threshold(gray,LimiarBinarizacao,255,cv2.THRESH_BINARY)[1]
      FrameBinarizado = cv2.dilate(FrameBinarizado,None,iterations=2)
      FrameBinarizado = cv2.bitwise_not(FrameBinarizado)
      _, cnts, _ = cv2.findContours(FrameBinarizado.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      cv2.drawContours(self.img,cnts,-1,(255,250,255),3)
      for c in cnts:
	    #se a area do contorno capturado for pequena, nada acontece
	    if cv2.contourArea(c) < AreaContornoLimiteMin:
        	continue
            
            QtdeContornos = QtdeContornos + 1

	    #obtem coordenadas do contorno (na verdade, de um retangulo que consegue abrangir todo ocontorno) e
	    #realca o contorno com um retangulo.
	    (x, y, w, h) = cv2.boundingRect(c)   #x e y: coordenadas do vertice superior esquerdo
	                                         #w e h: respectivamente largura e altura do retangulo

            cv2.rectangle(self.img, (x, y), (x + w, y + h), (100, 255, 0), 2)
	
	    #determina o ponto central do contorno e desenha um circulo para indicar
	    CoordenadaXCentroContorno = (x+x+w)/2
	    CoordenadaYCentroContorno = (y+y+h)/2
	    PontoCentralContorno = (CoordenadaXCentroContorno,CoordenadaYCentroContorno)
	    cv2.circle(self.img, PontoCentralContorno, 1, (0, 100, 250), 5)
        
    	    DirecaoASerTomada = CoordenadaXCentroContorno - (width/2)   #em relacao a linha central
     
      #output da imagem
      #linha em azul: linha central / referencia
      #linha em verde: linha que mostra distancia entre linha e a referencia
      cv2.line(self.img,(width/2,0),(width/2,height),(255,150,0),2)
    
      if (QtdeContornos > 0):
            cv2.line(self.img,PontoCentralContorno,(width/2,CoordenadaYCentroContorno),(65,255,0),1)
    
      cv2.imshow('Detect Line',self.img)
      cv2.waitKey(10)
      return DirecaoASerTomada, QtdeContornos

   def TratarCircle(self):
    blurred = cv2.GaussianBlur(self.img, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    center = None
    if len(cnts) > 0:
      c = max(cnts, key=cv2.contourArea)
      ((x, y), radius) = cv2.minEnclosingCircle(c)
      M = cv2.moments(c)
      center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
      print "               circle detect ",center
      valor =  "circle detect ",center
      if radius > 10:
        cv2.circle(self.img, (int(x), int(y)), int(radius),(0, 255, 255), 2)
        cv2.circle(self.img, center, 5, (0, 255, 255), -1) 
    else:
      print "               circle not detect"
      valor =  "circle not detect",0
           
  # show the frame to our screen

    cv2.imshow("Detect Circle", self.img)
    cv2.waitKey(10)
    return valor
 
  # if the 'q' key is pressed, stop the loop
    
 
    
