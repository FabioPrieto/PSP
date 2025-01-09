persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

telefono = input("Por favor, introduce tu número de teléfono: ")
persona["telefono"] = telefono

print(f"{persona['nombre']} tiene {persona['edad']} años, vive en {persona['ciudad']} y su número de teléfono es {persona['telefono']}.")
