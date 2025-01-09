def prefijo_comun_mas_largo(cadenas):
    if not cadenas:
        return ""
    
    prefijo = cadenas[0]
    
    for cadena in cadenas[1:]:
        while cadena[:len(prefijo)] != prefijo and prefijo:
            prefijo = prefijo[:-1]
    
    return prefijo

# Ejemplo de uso
lista_cadenas = ["flower", "flow", "flight"]
prefijo = prefijo_comun_mas_largo(lista_cadenas)
print("El prefijo común más largo es:", prefijo)
