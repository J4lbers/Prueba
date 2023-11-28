def count_number (n):
        cantidad = len(str(n))
        if cantidad == 8:
                print("Inserto correctamente la cantidad de digitos")
        else:
                print("Hubo un errror en la cantidad de digitos")
numero = int(input("Ingrese su DNI:"))
count_number(numero)