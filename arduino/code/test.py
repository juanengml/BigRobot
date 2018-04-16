import serial
import psutil

bat = psutil.sensors_battery()[0]
import os
try:
 ser = serial.Serial("/dev/ttyACM0",9600)
except:
 try:
   ser = serial.Serial("/dev/ttyACM2",9600)
 except:
   try:
      ser = serial.Serial("/dev/ttyUSB0",9600)
   except:
      print "FAIL MODA FOKA SERIAL USB"
      pass


while True:
  print "STATUS BATERIA: %2.2f" % bat
  m = raw_input("0 - sair\nw - frente\ns - voltar\na - direta\nd - esquerda\np - parar\nf - pedir licenca\nComando ==> ")
  if m=='0':break
  if m=="w":
    ser.write("w")
  if m=='s':
    ser.write("s")
  if m=='a':
    ser.write("a")
  if m=='d':
    ser.write("d")
  if m=='p':
    ser.write("p")
  if m=="f":
     os.popen("nice espeak -a300 -s 130 -vpt+m2 'Ola tudo bem, voce poderia me dar licensa'")    
