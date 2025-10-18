def contarpares(lista):
    cont = 0
    for x in lista:
        if x % 2 == 0:
            cont += 1
    return cont

lista = [1,2,3,4,5,6,7,8]
print(lista)
ret = contarpares(lista)
print(ret)