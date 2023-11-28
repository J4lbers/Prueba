#creacion de diccioonario
#dict(key,value)
from turtle import clear


diccionario={
    "Hardware":"parte dura de la pc",
    "Software":"parte blanda de la pc",
    "Periferocos":"dispositivos externos que se conecten a la pc",
    }
print(diccionario)

#largo
print(len(diccionario))

#accerder aun elemento
print(diccionario("Software"))

#modificar elemento
diccionario["Software"]="parte logical de la pc"
print(diccionario["Software"])

#limpiar
diccionario,clear()
print(diccionario)

#eliminar el diccionario
del diccionario
print(diccionario)