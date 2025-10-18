def analize(cadena):
    lwords = cadena.lower().split()
    stats = {'nlines' : len(cadena.splitlines()), 
            'nwords' : len(lwords),
            'nchars' : len(cadena),
            'vocab' : {word : lwords.count(word) for word in set(lwords)} ,
            'vocab_ch' : {char : cadena.count(char) for char in set(cadena)} ,
            }
    
    
    return stats      
        
print(analize('Hola soy Alarcon y soy de 2º\nhooooooolaaaa hola\n'))
