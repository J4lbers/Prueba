num_1 =int(input("Inserte primer número:"))
num_2 =int(input("Inserte segundo número:"))
num_3 =int(input("Inserte tercer número:"))
if (num_1 > num_2 and num_1 < num_3):
    print("El número mayor es:", num_1)
elif (num_2 > num_3 and num_2 > num_1 ):
    print("El número mayor es:", num_2)
else:
    print("El número mayor es:", num_3)