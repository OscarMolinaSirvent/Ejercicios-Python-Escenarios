from Ejercicio4 import analize
import json
import sys

def analize_from_file(ruta_fichero_txt,fichero_json=sys.stdout):
    with open(ruta_fichero_txt, "r") as fich:
        contenido = analize(fich.read())
        json_str = json.dumps(contenido)
    
    if fichero_json != sys.stdout:
        with open(fichero_json,"w") as fich:
            fich.write(json_str)
    else:
        sys.stdout.write(json_str)
       
