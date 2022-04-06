from operator import truediv
from traceback import print_tb
import conv_json
import serial
import time
import readjson
import compjson
import storejson

def transmision(vectorn):#vector nuevo 
    # convierto el vector nuevo a json (en realidad a dict)
    vectorn = conv_json.dataToJson(vectorn)
    # leo el vector anterior
    vectora = readjson.leojson('vectora.json')#leo el json de los datos anteriores
    # comparo ambos diccionarios para seleccionar el gcode
    resultado = compjson.compjson(vectorn,vectora)
    print("[M, X, Y, Z] => ", resultado)
    # guardo el arreglo actual como anterior para la proxima iteracion
    storejson.store(vectorn)

    comando = "Ya se encuentra en la posición seleccionada"#esta variable contine el strign que se debe enviar por el puerto serie
    # si se selecciono una muestra se escoje la coordenada absoluta que corresponda
    if resultado[0]!=0:
        if resultado[0]==1:#se deben enviar las coordenadas absolutas correspondientes a la muestra 1
            comando = "$J=G21G90X0.01Y0.01Z0.01F10\r\n"
        if resultado[0]==2:#se deben enviar las coordenadas absolutas correspondientes a la muestra 2
            comando = "$J=G21G90X0.02Y0.02Z0.02F10\r\n"
        if resultado[0]==3:#se deben enviar las coordenadas absolutas correspondientes a la muestra 3
            comando = "$J=G21G90X0.03Y0.03Z0.03F10\r\n"
        if resultado[0]==4:#se deben enviar las coordenadas absolutas correspondientes a la muestra 4
            comando = "$J=G21G90X0.04Y0.04Z0.04F10\r\n"
        if resultado[0]==5:#se deben enviar las coordenadas absolutas correspondientes a la muestra 5
            comando = "$J=G21G90X0.05Y0.05Z0.05F10\r\n"
        if resultado[0]==6:#se deben enviar las coordenadas absolutas correspondientes a la muestra 6
            comando = "$J=G21G90X0.06Y0.06Z0.06F10\r\n"
        if resultado[0]==7:#se deben enviar las coordenadas absolutas correspondientes a la muestra 7
            comando = "$J=G21G90X0.07Y0.07Z0.07F10\r\n"
        if resultado[0]==8:#se deben enviar las coordenadas absolutas correspondientes a la muestra 8
            comando = "$J=G21G90X0.1Y0.1Z0.1F10\r\n"
    
    # Si el cambio fue incremental se determina el eje al que corresponde y si es negativo o positivo
    if resultado[1]!=0:#corresponde al eje X
        if resultado[1]>0:
            comando = "$J=G21G91X0.01F10\r\n" #solo movimiento positivo en X 
        if resultado[1]<0:
            comando = "$J=G21G91X-0.01F10\r\n" #solo movimiento negativo en X 
    if resultado[2]!=0:#corresponde al eje Y
        if resultado[2]>0:
            comando = "$J=G21G91Y0.01F10\r\n" #solo movimiento positivo en Y 
        if resultado[2]<0:
            comando = "$J=G21G91Y-0.01F10\r\n" #solo movimiento negativo en Y 
    if resultado[3]!=0:#corresponde al eje Z
        if resultado[3]>0:
            comando = "$J=G21G91Z0.01F10\r\n" #solo movimiento positivo en Z 
        if resultado[3]<0:
            comando = "$J=G21G91Z-0.01F10\r\n" #solo movimiento negativo en Z 
    print ("Código a enviar: ", comando)
   
    # # Transmision serie después del filtrado de los valores
    try:
        ser = serial.Serial('COM4', 115200)
        time.sleep(1)
        ser.write(str.encode(comando)) #ir al home
        time.sleep(1)
        ser.close()
    except:
        print("Pueto COM incorrecto o dispositivo sin conectar")
    
    # # # ser.write(str.encode("$J=G21G91Y-0.01F10\r\n")) #solo y
    # # # # ser.write("X0.5\r\n")
    # # # time.sleep(2)
    # # # ser.write(str.encode("$J=G21G91Z-0.01F10\r\n"))#solo z
    # # # print("enter")
    # # # flag = input()
    # # # J
    # # # G21
    # # # G90 posicion absoluta
    # # # G91 posicion relativa
    # # # F10
    
    

    # # import serial
    # # import time

    # # ser = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
    


    # # def write_read(x):
    # #     ser.write(bytes(x, 'utf-8'))
    # #     time.sleep(0.05)
    # #     data = ser.readline()
    # #     return data

    # # while True:
    # #     num = input("Enter a number: ")
    # #     value = write_read(num)
    # #     print(value)
# f = open('sig.txt','r')
# vectorn = f.read()
# f.close()
# transmision(vectorn)

