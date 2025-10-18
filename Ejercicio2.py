def pares_impares(lista):
    lista_pares , lista_impares = [], []
    
    for x in lista:
        if x % 2 == 0:
            lista_pares.append(x)
        else:
            lista_impares.append(x)
    
    return lista_pares,lista_impares

lista = list(range(1,10))
print(lista)
ret = pares_impares(lista)
print(ret)