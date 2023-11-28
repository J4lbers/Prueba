#crear la clase calculadora
"""
class Calculadora():
    def _int_(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def por(self):
        print(self.num1*self.num2)
micalculadora=Calculadora(17,7)
micalculadora.por()
"""
#hallar el area de un rectangulo
from tkinter import ANCHOR


class prismarect:
    def _init_(self,base,altura,ancho,):
            self.base = base
            self.altura = altura
            self.ancho = ancho
            
    def calcular_prisma(self):
            return self.base*self.altura*self.ancho
    base = (int(input("Proporcione la base:")))
    altura = (int(input("Proporcione la altura:")))
    ancho = (int(input("Proporcione la ancho:")))
rectangulo1=prismarect(base,altura,ancho)
print(f"Area del prisma:{rectangulo1.calcular_prisma()}")
#prisma recto Juan Alberto Quispe Condori
#problema final