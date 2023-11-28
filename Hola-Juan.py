def cuenta_regresiva(num):
    num-=1
    if num>-1:
        print(num)
        cuenta_regresiva(num)
    else:
            print("Se termino el tiempo")
            print("fin de la funcion")
cuenta_regresiva(1000)