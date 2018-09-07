import obrcv

cam = obrcv.Camera(True,False,False)

while True:
    Direcao,TemLinha = cam.Line()
    if (Direcao > 0):
              print "[DIREITA]"
    if (Direcao < 0):
              print "[ESQUERDA]"      
    if (Direcao == 0):
              print "Exatamente na linha"
    
    

