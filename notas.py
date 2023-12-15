"""
PROGRAMA PARA CALCULAR LAS NOTAS DE N ESTUDIANTES..
"""
import os
alumnos = []
isActive = True
menu = "1. Registrar Alumno\n2. Registrar Nota\n3. Salir\n:"
subMenuNotas = ["Parciales","Quices","Trabajos","Regresar al menu principal"]
opMenu = 0
while (isActive):
    os.system("cls")
    try:
        opMenu = int(input(menu))
    except:
        print("Error en el dato de ingreso")
        os.system("pause")
    else:
        if (opMenu == 1):
            pass
        elif (opMenu == 2):
            opNotas = 0
            isActiveGrades = True
            while (isActiveGrades):
                for i,item in enumerate(subMenuNotas):
                    print(f"{i+1}. {item}")
                try:
                    opNotas = int(input(":)"))
                except:
                    print("Error en el dato de ingreso")
                    os.system("pause")
                else:
                    if (opNotas == 1):
                        pass
                    elif (opNotas == 2):
                        pass
                    elif (opNotas == 3):
                        pass
                    elif (opNotas == 4):
                        isActiveGrades = False
                    else:
                        pass
        elif (opMenu == 3):
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            print("Opcion invalida")
    os.system("pause")

