print("Bienvenido vamos a jugar")
print("Escoja")
jugador = input("Selecione que va a jugar suma(+),resta(-) o adivinar un número(a)")
if jugador =="-":
    a = int(input("¿cuanto es 10-5:"))
    if a == 5:print("El número es correcto ganó")
    else:
        print("El número es incorrecto perdio")
elif jugador =="+":
    b = int(input("Cunto es la suma de 17 + 3 ="))
    if  b == 20:
        print("El número es correcto ganó")
    elif b != 20:
        print("El número es incorrecto perdio")
elif jugador == "a":
    c = 30
    d = 0
    while c != d:
        d =(int(input("Adivine el número es :")))
        if d == c:
            print("El número es correcto ganó")
        elif d<c:
            print("El número es menor")
        else:
            print("El número es mayor")