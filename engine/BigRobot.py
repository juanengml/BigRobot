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
  def __init__(self,direcao):
   self.direcao = direcao
  def mover(self):
   if self.direcao == 'w':
      print "w -  FRENTE"
      STATUS_COM('w')

   if self.direcao == "s": 
      print "s - RE"
      arduino.write('s')

   if self.direcao == "a":
      print "a - ESQUERDA"
      arduino.write('a')

   if self.direcao == "d":
      print "d - direita "
      arduino.write('d')

   if self.direcao == "p":
      print "p - stop"
      arduino.write('p')

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