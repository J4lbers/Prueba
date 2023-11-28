#definir una lista de tipo str
nombres=["Juan", "Karla", "Ricardo", "María"]
print(nombres)
#aceder alos elementos de una lista
print(nombres[0])
print(nombres[1])
print(nombres[2])
#acederalos elementos de manera inversa
print(nombres[-2])
#imprimir un rango
print(nombres[0:2])
#ir del inicio de la lista al indice ....sin incluirlo
print(nombres[ :2])
#desde el indice indica hasta el final
print(nombres[1: ])
#cambiar el valor
nombres[3] = "ivone"
#iterar una lista
for nombre in nombres:
    print(nombres)
else:
    print("NO VALUE")

#PREGUNTAR ELLARO DELALISTA
print(len(nombres))

#agregar un elemento
nombres.append("Lorenzo")
#insetar un elemento en un indice en especific
nombres.insert("Octavio")
#remover un elemento
nombre.remover("Octavio")
#remover el ultimovalor agraado
nombre.pop("Octavio")
print(nombres)
#