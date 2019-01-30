import cv2
import numpy as np

LimiarBinarizacao = 125       #este valor eh empirico. Ajuste-o conforme sua necessidade 
AreaContornoLimiteMin = 5000  #este valor eh empirico. Ajuste-o conforme sua necessidade 

#Funcao: trata imagem e retorna se o robo seguidor de linha deve ir para a esqueda ou direita
#Parametros: frame capturado da webcam e primeiro frame capturado
#Retorno: < 0: robo deve ir para a direita
#         > 0: robo deve ir para a esquerda
#         0:   nada deve ser feito
def TrataImagem(img):
    #obtencao das dimensoes da imagem
    height = np.size(img,0)
    width= np.size(img,1)
    QtdeContornos = 0
    DirecaoASerTomada = 0
    
    #tratamento da imagem
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    FrameBinarizado = cv2.threshold(gray,LimiarBinarizacao,255,cv2.THRESH_BINARY)[1]
    FrameBinarizado = cv2.dilate(FrameBinarizado,None,iterations=2)
    FrameBinarizado = cv2.bitwise_not(FrameBinarizado)
    
    #descomente as linhas abaixo se quiser ver o frame apos binarizacao, dilatacao e inversao de cores
   # cv2.imshow('F.B.',FrameBinarizado)
   # cv2.imshow('F.B.1',gray)
    
   # cv2.waitKey(10)

    _, cnts, _ = cv2.findContours(FrameBinarizado.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   # cv2.drawContours(img,cnts,-1,(255,0,255),3)
    print (cnts)
    for c in cnts:
	    #se a area do contorno capturado for pequena, nada acontece
	    if cv2.contourArea(c) < AreaContornoLimiteMin:
        	continue
            
            QtdeContornos = QtdeContornos + 1

	    #obtem coordenadas do contorno (na verdade, de um retangulo que consegue abrangir todo ocontorno) e
	    #realca o contorno com um retangulo.
	    (x, y, w, h) = cv2.boundingRect(c)   #x e y: coordenadas do vertice superior esquerdo
	                                         #w e h: respectivamente largura e altura do retangulo

            #cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #cv2.imshow("Line",img) 
	    #determina o ponto central do contorno e desenha um circulo para indicar
	    CoordenadaXCentroContorno = (x+x+w)/2
	    CoordenadaYCentroContorno = (y+y+h)/2
	    PontoCentralContorno = (CoordenadaXCentroContorno,CoordenadaYCentroContorno)
	    cv2.circle(img, PontoCentralContorno, 1, (0, 3, 0), 5)
	    #cv2.imshow("Line",img)
        
    	    DirecaoASerTomada = CoordenadaXCentroContorno - (width/2)   #em relacao a linha central
     
    #output da imagem
    #linha em azul: linha central / referencia
    #linha em verde: linha que mostra distancia entre linha e a referencia
    cv2.line(img,(width/2,0),(width/2,height),(255,0,0),2)
    #cv2.imshow("Line",img)
    if (QtdeContornos > 0):
        cv2.line(img,PontoCentralContorno,(width/2,CoordenadaYCentroContorno),(0,255,0),1)
    
    
    cv2.imshow('Analise de rota DA OBR',img) 
    cv2.waitKey(10)
    return DirecaoASerTomada, QtdeContornos


#Programa principal


#camera = cv2.VideoCapture("simulacao.mp4")
camera = cv2.VideoCapture(0)
camera.set(3,320)
camera.set(4,240)


#fourcc = cv2.VideoWriter_fourcc(*'XVID')

#out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))


#faz algumas leituras de frames antes de consierar a analise
#motivo: algumas camera podem demorar mais para se "acosumar a luminosidade" quando ligam, capturando frames consecutivos com muita variacao de luminosidade. Para nao levar este efeito ao processamento de imagem, capturas sucessivas sao feitas fora do processamento da imagem, dando tempo para a camera "se acostumar" a luminosidade do ambiente
for i in range(0,20):
    (grabbed, Frame) = camera.read()

while True:
    
    try:
      (grabbed, Frame) = camera.read()
      if cv2.waitKey(1) & 0xFF == ord('q'):
            break
      if (grabbed):
          Direcao,QtdeLinhas = TrataImagem(Frame)
#          out.write(Frame)
          if (QtdeLinhas == 0):
             print "Nenhuma linha encontrada. O robo ira parar."
             continue
        
          if (Direcao > 0):
              print "Distancia da linha de referencia: "+str(abs(Direcao))+" pixels a [DIREITA]"
          if (Direcao < 0):
              print "Distancia da linha de referencia: "+str(abs(Direcao))+" pixels a [ESQUERDA]"      
          if (Direcao == 0):
              print "Exatamente na linha de referencia!"      
    except (KeyboardInterrupt):
          print "STOP MODA FOCA"
          break;

#out.release()
camera.release()
cv2.destroyAllWindows()
exit(1)   
