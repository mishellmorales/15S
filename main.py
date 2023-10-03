informacion_personal = {
    "Nombre": "Mishell Morales",
    "Edad": 25,
    "Ciudad": "Puyo",
    "Profesion":""
}

informacion_personal["Ciudad"] = "Santo Domingo"
informacion_personal["Profesion"] = "Contadora"

# Verificar si "telefono" no está presente y luego agregarlo
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0967145312"

# Verificar si "edad" está presente y luego eliminarlo
if "Edad" in informacion_personal:
    del informacion_personal["Edad"]

print(informacion_personal)