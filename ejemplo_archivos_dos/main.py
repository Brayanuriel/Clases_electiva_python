import funciones

archivo = "archivo_ejemplo_brayan.csv"

while True:
    print("menu")
    print("1 ver estudiantes")
    print("2 agregar estudiantes")
    print("3 salir")
    
    opcion = input(" seleccione una opcion:")
    
    if opcion =="1":
        ests = funciones.leer_estudiantes(archivo)
        for e in ests:
            print(f"{e["su nombre es"]}-{e["su edad es "]} años- {e[direccion]}")
            
            
    elif opcion == "2":
        nombre = input("nombre:")
        edad= input ("edad:")
        direccion =input ("direccion:")
        
        
        if not funciones. validar_nombre(nombre):
            print("⚠️ nombre invalido")
        continue
    
        if not funciones. validar_edad(edad):
            print("⚠️ edad invalido")
            continue
    
        if not funciones. validar_direccion(direccion):
            print("⚠️ direccion invalido")
            continue
    
    
        funciones.agregar_estudiante(archivo, nombre, edad, direccion)
        print("Estudiantes agregados con exito")
    
    elif opcion == "3":
        break

    else:
        print("opcion no valida")
    
    
        