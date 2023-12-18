"""
PROGRAMA PARA CALCULAR LAS NOTAS DE N ESTUDIANTES..
"""
import os
alumnos = []
isActive = True
menu = "1. Registrar Alumno\n2. Registrar Nota\n3. Buscar Alumno\n4. Notas Finales\n5. Salir\n:)"
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
                parciales = []
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
                except ValueError:
                    print("Error en el dato de ingreso")
                    os.system("pause")
                else:
                    if (opNotas == 1):
                        rta = "S"
                        isAddGrades = True
                        while isAddGrades:
                            codigo = input("Ingrese el codigo del Estudiante: ")
                            for item in alumnos:
                                if codigo in item:
                                    indice = alumnos.index(item)
                            while (rta in ["S","s"]):
                                nota = float(input("Ingrese la nota del Parcial: "))
                                alumnos[indice][3].append(nota) 
                                os.system("pause")
                                rta = input("Desea registrar otra nota de parciales? S(si) o N(no)").upper()
                            if bool(input("Desea registrar otro Estudiante S(Si) o Enter(No): ")):
                                rta = "S"
                                isAddGrades = True
                            else:
                                isAddGrades = False
                    elif (opNotas == 2):
                        rta = "S"
                        isAddGrades = True
                        while isAddGrades:
                            codigo = input("Ingrese el codigo del Estudiante: ")
                            for item in alumnos:
                                if codigo in item:
                                    indice = alumnos.index(item)
                            while (rta in ["S","s"]):
                                nota = float(input("Ingrese la nota del Quiz: "))
                                alumnos[indice][4].append(nota) 
                                os.system("pause")
                                rta = input("Desea registrar otra nota de quices? S(si) o N(no)").upper()
                            if bool(input("Desea registrar otro Estudiante S(Si) o Enter(No): ")):
                                rta = "S"
                                isAddGrades = True
                            else:
                                isAddGrades = False
                    elif (opNotas == 3):
                        rta = "S"
                        isAddGrades = True
                        while isAddGrades:
                            codigo = input("Ingrese el codigo del Estudiante: ")
                            for item in alumnos:
                                if codigo in item:
                                    indice = alumnos.index(item)
                            while (rta in ["S","s"]):
                                nota = float(input("Ingrese la nota del Trabajo: "))
                                alumnos[indice][5].append(nota) 
                                os.system("pause")
                                rta = input("Desea registrar otra nota de trabajos? S(si) o N(no)").upper()
                            if bool(input("Desea registrar otro Estudiante S(Si) o Enter(No): ")):
                                rta = "S"
                                isAddGrades = True
                            else:
                                isAddGrades = False
                    elif (opNotas == 4):
                        isActiveGrades = False

                    elif (opNotas == 5):
                        isActiveGrades = False
                    else:
                        print("Opcion invalida")                
                os.system("pause")
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

