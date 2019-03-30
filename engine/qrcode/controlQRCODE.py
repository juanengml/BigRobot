#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zbar 
from PIL import Image 
import cv2 
comp = open("dados","rb").read().split("\n\n")[0].split("\n") 

def main():
    capture = cv2.VideoCapture(1) 
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break
        ret, ibagem = capture.read() 
        gray = cv2.cvtColor(ibagem, cv2.COLOR_BGR2GRAY) 
        image = Image.fromarray(gray)  
        width, height = image.size 
        zbar_image = zbar.Image(width, height, 'Y800', image.tostring()) 
        scanner = zbar.ImageScanner() 
        scanner.scan(zbar_image) 
        cv2.imshow('Detect QRCODE', ibagem)
        cv2.imshow('gray', gray)

        for decoded in zbar_image: 
            text = decoded.data  
            print text
            for p in range(len(comp)):  
                if text == comp[p]:
                   print "TEXT:",text,"\t COMPARAR:",comp[p] 

if __name__ == "__main__": # EXECUTA A FUNÇÃO 
    main()
