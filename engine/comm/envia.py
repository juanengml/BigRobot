# -*- coding: cp1252 -*-
import paho.mqtt.client as mqtt
import random
from time import sleep
import datetime
import pyautogui

client = mqtt.Client()
# conecta no broker
client.connect("192.168.0.14", 1883)

# "bloco/E/lab/302/SENSOR/JANELA/1
# "home/sala/janela/01/status/"
niveis = {1:"arido",
 2:"seco",
 3:"umido",
 4:"molhado"}


while True:
    menu = pyautogui.confirm(text='Status Comandos',title='Simulador BigRobot V1 MQTT', buttons=['RUN', 'LEFT','RIGHT','STOP','SAIR'])
        #buttons=['arido', 'seco','umido','molhado','SAIR','reset'])     
    if menu=='RUN':
       print menu
       client.publish("/bigrobot/v1/status/", menu)       
    if menu=='LEFT':
       print menu
       client.publish("/bigrobot/v1/status/", menu)       
    if menu=='RIGHT':
       print menu
       client.publish("/bigrobot/v1/status/", menu)       
    if menu=='STOP':
       print menu
       client.publish("/bigrobot/v1/status/", menu)       

    if menu=='SAIR': 
        print "EXIT PROGRAMMM"
        break


  