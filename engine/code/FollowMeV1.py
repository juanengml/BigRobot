import dlib
import sys
import cv2
import serial

font = cv2.FONT_HERSHEY_SIMPLEX
pulaquadros = 0.5
captura = cv2.VideoCapture(0)
contadorquadros = 0
detector = dlib.simple_object_detector("../classificadores/classificador_bigrobot2.svm")

arduino = serial.Serial("/dev/ttyACM0",9600)


def controle_motores(e,t,d,f,comandos):
  if e > 300 and t > 300:
  	#arduino.write(comandos)
  if d > 300 and f > 200:
  	#arduino.write(comandos)

while captura.isOpened():
	conectado, frame = captura.read()
#	contadorquadros += 1
#	if contadorquadros % pulaquadros == 0:
	objetosdetectados = detector(frame, 1)
	for o in objetosdetectados:
			e, t, d, f = (int(o.left()), int(o.top()), int(o.right()), int(o.bottom()))
			print (e,t)
			print (d,f)	
			cv2.rectangle(frame, (e, t), (d, f), (0, 101, 255), 2)
			#cv2.putText(frame,"Big Robot", (e,t), cv2.FONT_HERSHEY_SIMPLEX, 1, 155)
			cv2.putText(frame,'Big Robots',(e,t), font, 2,(21, 101, 192),2,cv2.LINE_AA)

	cv2.imshow("logo bigrobots", frame)

	if cv2.waitKey(1) & 0xFF == 27:
			break

captura.realease()
cv2.destroyAllWindows()
sys.exit(0)