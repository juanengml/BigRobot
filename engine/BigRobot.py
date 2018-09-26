import serial
import psutil

status = False

try:
   arduino = serial.Serial("/dev/ttyACM0",9600)
   status = True
   print "PORTA COM /dev/ttyACM0 ENCONTRADA"
except:
   try:
    arduino = serial.Serial("/dev/ttyACM1",9600)
    status = True
    print "PORTA COM /dev/ttyACM1 ENCONTRADA"
   except:
    arduino = ""
    status = False
 



class Move:
  def __init__(self,comand,direcao):
   self.direcao = direcao
   self.comand = comand
 
  def mover(self):
   if self.comand == "w":
      print "w -  FRENTE"   
      if status == True:
        arduino.write("w")
        print "COMANDO ENVIADO:  ",self.comand
      else:
        print "PORTA COM ARDUINO NAO DETECTADO"

   if self.comand == "s": 
      print "s - BACK"
      if status == True:
        arduino.write("s")
        print "COMANDO ENVIADO:  ",self.comand
      else:
        print "PORTA COM ARDUINO NAO DETECTADO"

   if self.comand == "a":
      print "a - ESQUERDA"
      if status == True:
        arduino.write("a")
        print "COMANDO ENVIADO:  ",self.comand
      else:
        print "PORTA COM ARDUINO NAO DETECTADO"

   
   if self.comand == "d":
      print "d - direita "
      if status == True:
        arduino.write("d")
        print "COMANDO ENVIADO:  ",self.comand
      else:
        print "PORTA COM ARDUINO NAO DETECTADO"


   if self.comand == "p":
      print "p - stop"
      if status == True:
        arduino.write("p")
        print "COMANDO ENVIADO:  ",self.comand
      else:
        print "PORTA COM ARDUINO NAO DETECTADO"



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