from unittest import result
import readjson
# recibo dos diccionarios
def compjson(vectorn,vectora):
# def compjson():
#     #solo para reemplazar los vectores
#     vectorn = readjson.leojson('vectorn.json')
#     vectora = readjson.leojson('vectora.json')
    # print(type(vectora))
    # print(type(vectorn))
    # resultado = vectorn - vectora
    
    # conversion de str a int de las coordenadas para comparar mas facilmente
    vectorn ["muestra"] = int(vectorn["muestra"])
    vectorn ["X"] = int(vectorn ["X"])
    vectorn ["Y"] = int(vectorn ["Y"])
    vectorn ["Z"] = int(vectorn ["Z"])
    vectora ["muestra"] = int(vectora["muestra"])
    vectora ["X"] = int(vectora ["X"])
    vectora ["Y"] = int(vectora ["Y"])
    vectora ["Z"] = int(vectora ["Z"])
    #realizo la comparacion y la guardo en una lista que es lo que espera el transmisor
    resultado = [0, 0, 0, 0]
    if (vectorn["muestra"]==vectora["muestra"]):
        # si en el msj viene el mismo numero de muestra que el anteriror se toma como si no hubo cambio
        resultado[0] = 0
    else:
        # en caso de ser distintas quiere decir que fue el cambio que realizo el usuario
        resultado[0]=vectorn["muestra"]
    # Con la resta solo pasa 1 o -1 ya no es acumulativo
    resultado [1] = vectorn["X"] - vectora["X"]
    resultado [2] = vectorn["Y"] - vectora["Y"]
    resultado [3] = vectorn["Z"] - vectora["Z"]
    return resultado

# compjson()