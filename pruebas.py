cant = int(input("¿Cuantos parciales desea ingresar?: "))
parciales = []
for i in range(0,cant):
    notasParciales = int(input(f"Ingrese la nota del parcial {i+1}: "))
    parciales.append(notasParciales)                              
print(parciales)