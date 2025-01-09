from itertools import permutations

def encontrar_permutaciones(lista):
    return list(permutations(lista))

# Ejemplo de uso
mi_lista = [1, 2, 3]
permutaciones = encontrar_permutaciones(mi_lista)
print("Permutaciones de la lista:", permutaciones)