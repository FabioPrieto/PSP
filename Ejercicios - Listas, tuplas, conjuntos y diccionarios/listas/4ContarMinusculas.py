cadenas = ["Red", "Yellow", "Green", "Blue", "White", "Pink"]
cont = 0
for cadena in cadenas:
    for car in cadena:
        if car.islower():
            cont +=1

print(cont)