# -*- coding: cp1252 -*-
import paho.mqtt.client as mqtt
import serial
import psutil

TOPIC = "/robot/rover/"

client = mqtt.Client()
# conecta no broker
client.connect("192.168.100.3", 1883)


def STATUS_COM():

 status = False
 try:
   arduino = serial.Serial("/dev/ttyUSB0",9600)
   status = True
   print "Porta ttyUSB0"
 except:
   try:
    arduino = serial.Serial("/dev/ttyACM0",9600)
    print "Porta ttyACM0"
    status = True
   except:
    arduino = ""
    status = False
 return status




class Move:
  print STATUS_COM()
  def __init__(self,comand,direcao):
   self.direcao = direcao
   self.comand = comand
  
  def mover(self):
   lista = ["w","s","d","a","p"]     
   for p in range(len(lista)):
    if self.comand == lista[p]: 
      print p,lista[p]
      print (arduino.write(lista[p]) if STATUS_COM() else "Port not found !")
      client.publish(TOPIC,lista[p])



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