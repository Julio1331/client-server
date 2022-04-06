import json

# f = open ('sig.txt','r')
# vectora = f.read()
# print("leido",vectora)
# f.close()

def dataToJson(vectora): 
    vectora = vectora.replace('{"estado":[','')#elimino caracteres previos qye no uso
    vectora = vectora.replace(']}','')#elimino caracteres finales que no uso
    vectora = vectora.replace('"','')#elimino las comillas del primer elemento para que quede igual que los demas
    vectoraux=[1]#defino la lista de auxliares
    vectoraux[0] = vectora.partition(',')[0]#exraigo primer elemento
    vectora = vectora.replace(vectoraux[-1],'',1)#elimino el dato ya extraido, una sola vez porque puede estar repetido
    vectora = vectora.replace(',','',1)#elimino la coma que queda en el string
    ## extraccion del segungo elemento
    vectoraux.append(vectora.partition(',')[0])#exraigo segundo elemento
    vectora = vectora.replace(vectoraux[-1],'',1)#elimino el dato ya extraido, una sola vez porque puede estar repetido
    vectora = vectora.replace(',','',1)#elimino la coma que queda en el string
    ## extraccion del tercer elemento
    vectoraux.append(vectora.partition(',')[0])#exraigo  elemento
    vectora = vectora.replace(vectoraux[-1],'',1)#elimino el dato ya extraido, una sola vez porque puede estar repetido
    vectora = vectora.replace(',','',1)#elimino la coma que queda en el string
    ## ultimo elemento
    vectoraux.append(vectora)
    ##armo el diccionario y lo retorno
    dic = {'muestra':vectoraux[0], 'X':vectoraux[1], 'Y':vectoraux[2], 'Z':vectoraux[3] }
    return dic


# f = open('sig.txt','r')
# vectora = f.read()
# f.close()
# print(vectora)
# nuevo = dataToJson(vectora)
# print(nuevo)