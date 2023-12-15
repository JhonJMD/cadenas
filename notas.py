"""
PROGRAMA PARA CALCULAR LAS NOTAS DE N ESTUDIANTES..
"""
import os
alumnos = []
isActive = True
menu = "1. Registrar Alumno\n2. Registrar Nota\n3. Buscar Alumno\n4. Salir\n:"
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
            rta = ("S")
            while (rta in ["S","s"]):
                codigo = input("Ingrese el codigo del Estudiante: ")
                nombre = input("Ingrese el nombre del Estudiante: ")
                edad = int(input(f"Ingrese la edad del Estudiante {nombre}: "))
                alumno = [codigo,nombre,edad,[],[],[]]
                alumnos.append(alumno)
                print(alumnos)
                os.system("pause")
                rta = input("Desea registrar otro Alumno? S(si) o N(no)").upper()
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
            codigo = input("Ingrese el codigo del Estudiante: ")
            for item in alumnos:
                if codigo in item:
                    print(item)
            os.system("pause")
        elif (opMenu == 4):
            os.system("cls")
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            print("Opcion invalida")
    os.system("pause")

