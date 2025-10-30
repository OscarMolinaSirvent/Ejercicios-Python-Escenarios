import csv
import json

with open('Alcoi_dades_trafic_2022_T4.csv', 'r') as file:
    
    reader = csv.reader(file)
    next(reader)
    dic = {'vMin':1000, 'vMax':0, 'vMedia':0, 'EntradaCocentaina':0, 'SalidaCocentaina':0}    
    vSuma = 0
    vContador = 0
    velocidad = 0

    for linea in reader:
        
        velocidad = int(linea[3])
        if velocidad < dic['vMin']:
            dic['vMin'] = velocidad
        if velocidad > dic['vMax']:
            dic['vMax'] = velocidad
        vSuma += velocidad
        vContador += 1    
        
        if linea[4] == "AF_Entrada_Cocentaina":
            dic['EntradaCocentaina'] += 1
        if linea[4] == "AF_Salida_Cocentaina":
            dic['SalidaCocentaina'] += 1
        
    dic['vMedia'] = vSuma / vContador

json_str = json.dumps(dic)

with open("estadisticas.json","w") as file:
    file.write(json_str)

