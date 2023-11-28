#Módulos en Python
lista = list()
class Alumnos:
    def __init__(selt):
        selt.matricula=()
        selt.nombre=("")
        selt.edad=( )
        selt.especialidad=(" ")
def menu():
    seleccion = 0
    while seleccion != 4:
        print("bienvenidos al menu")
        print("eliga una opcion")
        print("1. regitrar alumnos")
        print ("2. mostrar alumnos")
        print("3. buscar alumnos")
        print("4. salir alumnos")
        seleccion = int(input("eliga una opcion: "))
        if seleccion == 1:
            registrar()
        elif seleccion == 2:
            mostrar()
        elif seleccion == 3:
            buscar()
        elif seleccion == 4:
            salir()
        else:
            break

def registrar ():
    print("esta funcion registra")
    alumno=Alumnos()
    alumno.matricula=input("introduce la matricula: ")
    alumno.nombre=input("introduce el nombre: ")
    alumno.edad=input("introduce la edad: ")
    alumno.especialidad=input("introduce la especialidad: ")
    lista.append(alumno)

def mostrar():
    print("esta funcion mostrar")
    for alumno in lista:
        print("Nombre: ", alumno.nombre )
        print("Matricula: ", alumno.matricula)
        print("Edad: ", alumno.edad)
        print("Especialidad: ", alumno.especialidad)

def buscar():
    print("esta funcion buscar")
    busqueda=input("ingrese la matricula o el nombre del alumno: ")
    for alumno in lista:
        if alumno.matricula==busqueda or alumno.nombre==busqueda:
            print(alumno.nombre,"-" , alumno.matricula ,"-", alumno.edad ,"-", alumno.especialidad)

def salir():
    print("cerrar menu")
menu()