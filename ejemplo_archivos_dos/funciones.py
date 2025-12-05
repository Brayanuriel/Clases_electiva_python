#validaacion de datos
def validar_nombre(nombre):
    return nombre.isalpha() and len(nombre)>= 2

def validar_edad(edad):
    return edad.isdigit() and 15 <= int (edad) <= 120

def validar_direccion(direccion):
    return len(direccion)>= 3

#leer archivos

def leer_estudiantes(archivo):
    lista = []
    with open (archivo,"r", encoding="utf-8") as f:
        next(f)# saltar el encabezado
        for linea in f:
            nombre, edad, direccion = linea.strip().split(",")
            lista.append({"nombre": nombre, "edad": edad, "direccion": direccion})
            return lista
        
# agregar estudiantes al csv

def agregar_estudiantes(archivo,nombre,edad,direccion):
    with open(archivo,"a", encoding="utf-8") as f:
        f.write(f"{nombre},{edad},{direccion}\n")