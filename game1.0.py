
gana = 18
jugador = 0
while gana != jugador:
    jugador=int(input("Adivine el número secreto "))
    if jugador > gana:
        print("El numero es mayor")
    elif jugador < gana:
        print("El numero es menor")
    else :
        print("Feliicitaciones encontraste el número que es 18") 
