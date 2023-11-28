"""
import random
n = random.randint(5,15)
print(n)

even_num = 0
odd_num = 0

while (n > 0):
    if n % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
        n=n //10
print("Números pares:", (even_num),"Numeros impares" ,(odd_num))


def pont(base,exponente):
    resultado = 1
    for i in range(exponente) :
        resultado *= base
    return resultado
print(2**3)
print(pow(2,3))
print(pont(2,3))
hghghghghghghghghghghghghghghghghghgh
[10:31] SOSA HUANCA, IVAN ALEXANDER
lista = []

contador = 0

final = 10

import random

while contador < final:

    contador +=1

    n=random.randint(0,final)

    lista.append(n)
    texto = ""
    print(lista)

listaPares = []

for i in lista:

    if i%2==0:

         texto = texto+str(i)+", "

         listaPares.append(i)
         print("Hay "+str(len(listaPares))+" números pares: "+texto)
"""

