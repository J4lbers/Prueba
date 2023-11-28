horas=int(input("Ingresa las horas: ")) 
turno=input("Ingrese el turno(m,t,n): ") 
salario=horas*37 
if turno=="m":     
        salario==horas*37 
elif turno=="t":     
        salario+=salario*0.2 
elif turno=="n":     
        salario+=salario*0.5 
if salario >=2000 and salario<=5000: 
    salario-=salario*0.15 
elif salario>=8000 and salario<=10000:     
    salario*=salario*0.17 
print("El salario del trabajador es: ",salario)
