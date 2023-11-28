num1 = int(input("Inserte primer número:"))
num2 = int(input("Inserte segundo número:"))
operación = input("ESCOJA suma(+), resta(-), multiplicación(x), division(/), resto(%):")
if operación =="+":
    print(num1 + num2)
elif operación =="-":
    print(num1 - num2)
elif operación =="x":
    print(num1 * num2)
elif operación =="/":
    print(num1 / num2)
elif operación == "%":
    print(num1 % num2)
#calculadora con finalidad