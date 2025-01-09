
def palindromo(palabra):
    palabraBien = ""
    for y in palabra:
        if(y !=" "):
            palabraBien += y
    palabraBien = palabraBien.lower()

    longitud = len(palabraBien)
    i=1
    palindromo = True
    for x in palabraBien:
        if(x !=palabraBien[longitud-i]):
            return False
        i += 1 
    
    return True

palabra = input("Escribe una frase:")



if(palindromo(palabra)):
    print(palabra+" es palindromo")
else:
    print(palabra+" no es palindromo")
    

