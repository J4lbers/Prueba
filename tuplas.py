#tuplas en python
#definir tupla
frustas=("naranja", "platano", "guayaba")
print(frustas)

#largo
print(len(frustas))

#acceder a un elemento de una tupla
print(frustas[0])

#rango
print(frustas[0:1])
#recortar elemento
for frusta in frustas:
    print(frusta)
#recorre elementos pero en una sola linea
#for frusta in frustas:
 #   print(frutas, end=" ")
#cambiar valor de una tupla
#fruta[0] = "pera"
#print(fruta)
frutaslista=list(frutas)
frutaslista[0]="pera"
frustas=tuple(frutaslista)
print(frutas)