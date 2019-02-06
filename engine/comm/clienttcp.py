#!/usr/bin/env python

import socket
import pyautogui

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = " "

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
 MESSAGE = pyautogui.confirm(text="CONTROLE BIG ROBOT",title='CONTROLE BIG ROBOT',buttons=["w","s","a","d","p"])
 #MESSAGE = raw_input("\nw - frente\ns - voltar\na - esquerda\nd - direita\np - parar\n=> ")
 s.send(MESSAGE)
 data = s.recv(BUFFER_SIZE)

s.close()

print "received data:", data
