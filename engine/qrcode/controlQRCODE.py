#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zbar # IMPORTA BIBLIOTECA PARA ANALISAR QRCODE #
from PIL import Image # IMPORTA BIBLIOTECA PARA DA IMAGEM #
import cv2 # IMPORTA BIBLIOTECA DE VISÃO COMPUTACIONAL PARA CONVERTER DADOS DA IMAGEM
comp = open("dados","rb").read().split("\n\n")[0].split("\n")  # LER DADOS SALVOS NO ARQUIVO DADOS

def main(): # FUNCAO MAIN PARA PROCESSAR IMAGEM
    
    capture = cv2.VideoCapture(1) # ACESSA CAMERA PARA CAPTURAR OS FRAMES

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'): # SE TECLA Q APERTADA ELE STOP O SERVICO
            break
        ret, ibagem = capture.read() # LER E GRAVA OS DADOS DA CAMERA
        gray = cv2.cvtColor(ibagem, cv2.COLOR_BGR2GRAY) # PEGA DADOS DA IBAGEM E PASSA PARAMETRO DE CONVERSÃO EM ESCALA DE CINZA
        image = Image.fromarray(gray)  # PEGA FRAME EM CINZA E PEGA OS VETORES DA IMAGEM
        width, height = image.size # PEGA AS DIMENSÕES DA IMAGEM
        zbar_image = zbar.Image(width, height, 'Y800', image.tostring()) # PEGA DADOS DE DIMENSÃO DA IMAGEM E TRANSFORMA EM STRING 
        scanner = zbar.ImageScanner() # CRIA UMA INSTANCIA DO ZBAR
        scanner.scan(zbar_image)  # APLICA ZBAR PARA MONTAR A IMAGEM E PROCESSAR QRCODE
        cv2.imshow('Detect QRCODE', ibagem)# USA IBAGEM PARA CRIAR UM CAIXA DE DIALOGO E MOSTRAR A IMAGEM
#        cv2.imshow('gray', gray)

        for decoded in zbar_image: # ZBAR_IMAGEM TEM MTS DADOS E PARA DECODED PRECISA ITERAR
            text = decoded.data  # ITERANDO DADO EXTRAI DATA PRA TEXTO DO QUE ESTA COODIFICADO NA INSTANCIA
#            print text
            for p in range(len(comp)):  # LEN DE COMP = LER NUMERO DE ITENS SALVOS DENTRO DO ARQUIVO DADOS E COMPARA COM A VARIAVEL TEXT
                if text == comp[p]:
                   print "TEXT:",text,"\t COMPARAR:",comp[p] # MOSTRA NA TELA 

if __name__ == "__main__": # EXECUTA A FUNÇÃO 
    main()
