import serial
import psutil


def STATUS_COM(decision):

 status = False
 try:
   arduino = serial.Serial("/dev/ttyUSB0",9600)
   status = True
 except:
   try:
    arduino = serial.Serial("/dev/ttyACM0",9600)
    status = True
   except:
    arduino = ""
    status = False
 if status == True:
        arduino.write(decision)
 if status == False:
        print "PORTA COM ARDUINO NAO DETECTADO"



class Move:
  def __init__(self,comand,direcao):
   self.direcao = direcao
   self.comand = comand
 
  def mover(self):
   if self.comand == "w":
      print "w -  FRENTE"
      STATUS_COM('w')

   if self.comand == "s": 
      print "s - BACK"
      STATUS_COM('s')

   if self.comand == "a":
      print "a - ESQUERDA"
      STATUS_COM('a')
   
   if self.comand == "d":
      print "d - direita "
      STATUS_COM('d')

   if self.comand == "p":
      print "p - stop"
      STATUS_COM('p')


class Sensores:
  def __init__(self,distancia, bateria,gps):
    self.distancia = distancia
    self.bateria = bateria
    self.gps = gps

  def bat(self):
   if self.bateria == True:
     bat = psutil.sensors_battery()[0]
     print   bat
   else: print "FAIL BAT"

  def distance(self):
     if self.distancia == True:
            cm = arduino.write("distancia")
            cm = cm
            return cm
  def gps(self):
    if self.gps == True:
        # GET COORDINATES ON GPS SENSOR
        #
        #
        pass