import serial
import psutil

try:
  arduino = serial.Serial("/dev/ttyUSB0",9600)
except:
  arduino = serial.Serial("/dev/ttyACM0",9600)
  try:
    arduino = serial.Serial("/dev/ttyACM1",9600)
  except:
    arduino = ""

class Move:
  def __init__(self,direcao):
   self.direcao = direcao
  def mover(self):
   if self.direcao == 'w':
      print "w -  FRENTE"
      arduino.write('w')

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
  def __init__(self,distancia, bateria):
    self.distancia = distancia
    self.bateria = bateria

  def bat(self):
   if self.bateria == True:
     bat = psutil.sensors_battery()[0]
     print   bat
   else: print "FAIL BAT"

  def distance(self):
     pass
