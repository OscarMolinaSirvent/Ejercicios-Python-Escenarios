import json
from Ejercicio5 import analize_from_file

def print_words_from_json(ruta_fichero_json):
    with open(ruta_fichero_json,"r") as fd:
        d_fromdisk = json.loads(fd.read())
        print(d_fromdisk["vocab"])

analize_from_file("Prueba.txt", "Json.json")
print_words_from_json("Json.json")

