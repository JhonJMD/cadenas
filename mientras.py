import os
#bandera
isActive = True
rta = 0
menu = "1. Sumar\n2. Restar\n0. Salir\n"
#Ciclo Mientras
while (isActive):
    try:
        os.system("cls")
        rta = int(input(menu))
    except ValueError:
        print("Error en el dato")
    else:
        if (rta == 1):
            print("Sumando")
        elif (rta == 2):
            print("Restando")
        elif (rta == 0):
            print("Ok chao")
            isActive = False
        else:
            print("La opcion que ingreso es invalida...")
        os.system("pause")
# while (isActive):
#     os.system("cls")
#     rta = input("Desea continuar con la ejecucion: S(si) o Enter(No)").upper()
#     while (rta not in "S"):
#         print("Ha ingresado una opcion invalida")
#         os.system("pause")
#         os.system("cls")
#         rta = input("Desea continuar con la ejecucion: S(si) o Enter(No)").upper()
#     if (bool(rta) == False):
#         isActive = bool(rta)    