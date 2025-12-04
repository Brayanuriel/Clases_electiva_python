#FUNCIONES

# def saludar(nombre):
#     return f"¡Hola,{nombre}!bienvenido a clase numero 8."

# mensaje=saludar("brayan")
# print(mensaje)

#CALCULADORA CON FUNCION

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division (a,b):
    if b !=0:
        return a/b
    else:    
        return"¡¡error!!- no se puede dividir entre cero"


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
        print("resultado",suma(primerNumero, segundoNumero))
    elif opcion == "2":
        print("resultado", resta(primerNumero, segundoNumero))
    elif opcion == "3":
        print("resultado", multiplicacion(primerNumero, segundoNumero))
    elif opcion == "4":
        print("resultado", division(primerNumero, segundoNumero))
    else :
        print("opcion no valida")
calculadora()
