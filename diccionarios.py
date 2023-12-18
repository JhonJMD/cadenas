alumnos = {}
alumno = {
    "codigo":"123",
    "nombre":"Juan",
    "edad":13,
    "notas":{
        "parciales":[3.0,4.5],
        "quices":[],
        "trabajos":[],
    }
}
# print(alumnos)
# print(alumno["notas"])
# print(alumno["notas"]["parciales"].append(3.0))
# print(alumno["notas"]["parciales"])
# alumno["edad"] = 14
# for item in alumno:
#     print(item)
# for key in alumno:
#     print(f"{key.capitalize()} : {alumno[key]}")
for key,valor in alumno.items():
    if(type(valor) == str) or (type(valor) == int):
        print(f"{key.capitalize()} : {valor}")
    if (type(valor) == dict):
        if (type(valor.get("parciales","No se encontro la data")) == list):
            print(valor)
        else:
            print("Error en la busqueda")
alumnos.update({alumno["codigo"]:alumno})
alumno = {
    "codigo":"126",
    "nombre":"Pedro",
    "edad":13,
    "notas":{
        "parciales":[3.0,4.5],
        "quices":[],
        "trabajos":[],
    }
}
alumnos.update(alumno)
print("Mostrando Informacion de Alumnos")
print(alumnos["123"])