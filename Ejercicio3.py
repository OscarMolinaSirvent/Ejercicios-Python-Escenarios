def contar_vocales_consonantes(cadena):
    cadena = cadena.lower().replace(" ","")
    print(cadena)
    vocales = "aeiouáéíóú"
    num_vocales, num_consonantes = 0,0

    for x in cadena:
        if x in vocales:
            num_vocales += 1
        else:
            num_consonantes += 1
    print(f"Vocales: {num_vocales}, Consonantes: {num_consonantes}")

Texto = 'Me Llamo Oscar'
contar_vocales_consonantes(Texto)
