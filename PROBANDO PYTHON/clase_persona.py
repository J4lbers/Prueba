class Persona:
          def __init__(self,nombre,distancia,sentarse):
                  self.nombre = nombre
                  self.distancia = distancia
                  self.sentado = sentarse
          
          def Llamar(self):
                  self.nombre = input("Como te llamas :")
                  print(self.nombre)

          def caminar(self):
                    self.distancia = input("Cuantos metros desea caminar :")
                    print("Usted a caminado: "+ self.distancia)
          
          def sentarse(self):
                    if self.sentado:
                            print("Usted se ha sentado")
                    else:
                            print("siga caminando")
                    return "bien"
perosna_1 = Persona("Pedro",15,False)

print(perosna_1.Llamar())
print(perosna_1.caminar())
print(perosna_1.sentarse())
