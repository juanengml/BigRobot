import obrcv
import BigRobot 

cam = obrcv.Camera(True,False,False)

run   = BigRobot.Move("w",1)
back  = BigRobot.Move("s",1)
left  = BigRobot.Move("a",1)
right = BigRobot.Move("d",1)
stop  = BigRobot.Move("p",1)


while True:
    Direcao,TemLinha = cam.Line()
    if (Direcao > 0):
              print "[DIREITA]"
              right.mover()              
    if (Direcao < 0):
              print "[ESQUERDA]"
              left.mover()                          
    if (Direcao == 0):
              print "Exatamente na linha"
              run.mover()
    
    

