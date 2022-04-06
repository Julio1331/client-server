import json
# lo guardo como objeto o archivo json
def store(objson):
    with open('vectora.json', 'w') as outfile:
        json.dump(objson, outfile)