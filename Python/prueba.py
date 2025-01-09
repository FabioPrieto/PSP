palindromo = input("Introduce una frase: ")
palindromo.lower()
palindromo2 = ""
for i in palindromo:
    if (i != " "):
        palindromo2+=i
        
print(palindromo2)