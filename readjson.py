import json
# abre el archivo .json y lo guarda en vector como tipo de dato dictionary
def leojson(nombre):
    with open(nombre) as json_file:
        vector = json.load(json_file)
    return vector
