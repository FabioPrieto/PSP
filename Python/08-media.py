media = 0
total = 0
num = 0
notas = []


while num >= 0:
    num = int(input("Escribe un número entre 0 y 10:"))
    if num >= 0:
        notas.append(num)

print("Notas originales:", notas)


notas_filtradas = []

for item in notas:
    print("Procesando:", item)
    if item >= 5:
        notas_filtradas.append(item)
        total += item

print("Notas filtradas (>= 5):", notas_filtradas)


if len(notas_filtradas) > 0:
    media = total / len(notas_filtradas)
else:
    media = 0

print("Media de notas:", media)