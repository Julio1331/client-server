#importar modulo de envio de datos
import serialcom

vectorn = [0, 0, 0, 0]
vectora = [0, 0, 0, 0]
while 1:
    print ("ingrese nuevo vector")
    vectorn[0] = int(input())
    vectorn[1] = int(input())
    vectorn[2] = int(input())
    vectorn[3] = int(input())
    serialcom.transmision(vectorn, vectora)
    vectora = vectorn