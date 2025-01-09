frutas_precios = {
    "Apple": 1.35,
    "Orange": 0.90,
    "Banana": 0.95,
    "Kiwi": 1.00
}

fruta = input("Introduce el nombre de una fruta (Apple, Orange, Banana, Kiwi): ")
kilos = float(input("Introduce el número de kilos: "))

if fruta in frutas_precios:
    precio_total = frutas_precios[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es: {precio_total:.2f} euros.")
else:
    print("La fruta no está disponible.")
