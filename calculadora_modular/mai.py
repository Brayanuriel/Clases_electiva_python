import funciones

def calculadora():
    print(" calcuoladora basica")
    print(" 1 suma")
    print(" 2 resta")
    print(" 3 multiplicacion")
    print(" 4 division")
    
    opcion= input("escriba una de las opciones anteriores (1-4) ")
    
    primerNumero = float(input("ingrese el primer numero:"))
    segundoNumero= float(input("ingrese el segundo numero:"))
    
    if opcion == "1":
        print("resultado", funciones.suma(primerNumero, segundoNumero))
    elif opcion == "2":
        print("resultado", funciones.resta(primerNumero, segundoNumero))
    elif opcion == "3":
        print("resultado", funciones.multiplicacion(primerNumero, segundoNumero))
    elif opcion == "4":
        print("resultado", funciones.division(primerNumero, segundoNumero))
    else :
        print("opcion no valida")
calculadora()


# from funciones import sumar, restar
# print(sumar(2,3),restar(5,3))

import funciones as fin 
print(fin.suma(2,3))