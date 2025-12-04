# textoejemplo="hola buenas noches"
# print(textoejemplo.upper())

# textoejemplo="Hola Buenas Noches"
# print(textoejemplo.lower())

# textoejemplo="Hola Buenas Noches"
# print(textoejemplo.replace("Noches","Tardes"))

# texto = "   hola  mundo   "
# limpio = texto.strip()
# print(limpio)

# texto = ">>>>hola  mundo<<<<"
# nuevo = texto.strip("><")
# print(nuevo)

# texto = "programar en python es divertido"
# pos = texto.find("python")
# print(pos)

# texto = "programar en python es divertido"
# pos = texto.find("casa")
# print(pos)

# palabra="python"
# print(palabra[0])    #Muestra el primer caracter
# print(palabra[0:3])  #muetra desde el indice 0 hasta el indice 2
# print(palabra[2:])   #desde el indice 2 hasta el ultimo
# print(palabra[-1])   #ultimo caracter

# palabra="programacion en python"
# print(len(palabra))

# numero=6
# print(f"tabla del numero{numero}")
# for i in range(1,11):
#     print(f"{numero} x {i}={numero*i}")

# numero_secreto=5
# intento=int(input("adivina el numero del 1 al 10:"))
# while intento !=numero_secreto:
#   print("incorrecto intenta otra vez")
#   intento=int(input("adivina el numero del 1 al 10:"))
# print(f"¡correcto! {numero_secreto} es el numero correcto")

# contador=0
# for i in range(5):
#     contador+=1
# print(f"el bucle se ejecuta {contador} veces")

# acumulador=0
# for i in range(5):
#     numero=int(input("ingresa un numero:"))
#     acumulador+=numero
# print(f"la suma total es : {acumulador}")

# estudiantes=["veronica","laura","antonio", "julian", "brayan","santiago"]
# print(estudiantes[0])
# print(estudiantes[1])
# print(estudiantes[5])

# estudiantes=["veronica","laura","antonio", "julian", "brayan","santiago"]
# print(estudiantes[-1])
# print(estudiantes[-2])
# print(estudiantes[-5])

# estudiantes=["veronica","laura","antonio", "julian", "brayan","santiago"]
# estudiantes.append("lisseth")
# print(estudiantes)

# estudiantes=["veronica","laura","antonio", "julian", "brayan","santiago"]
# estudiantes.insert(1,"Dario") # inserta la posisciobn 1 (osea la segunda posicion )
# print(estudiantes)

# estudiantes=["veronica","laura","antonio", "julian", "brayan","santiago"]
# estudiantes[1] ="Maria"
# print(estudiantes)

# estudiantes=["veronica","laura","antonio", "julian", "brayan","santiago"]
# estudiantes[1:4] ="Maria","Pedro","Juan"
# print(estudiantes)

# estudiantes=["veronica","laura","antonio", "julian", "brayan","santiago"]
# estudiantes.remove("antonio")
# print(estudiantes)

# estudiantes=["veronica","laura","antonio", "julian", "brayan","santiago"]
# estudiantes.pop(4)
# print(estudiantes)

# estudiantes=["veronica","laura","antonio", "julian", "brayan","santiago"]
# estudiantes.sort()
# print(estudiantes)

# estudiantes=["veronica","laura","antonio", "julian", "brayan","santiago"]
# estudiantes.sort(reverse=True)
# print(estudiantes)

# numeros=[]
# for i in range(5):
#     numero=int(input("ingrese un numero:"))
#     numeros.append(numero)
# print(f"la lista final es: {numeros}")

# persona={
#     "nombre": "Ana",
#     "edad": "20",
#     "ciudad": "bogota"
# }
# print(persona["nombre"])
# print(persona["edad"])

# estudiantes={"nombre":"laura","edad": 20,"nota":4.5}
# estudiantes["nota"]=4.8
# print(estudiantes)

# estudiantes={"nombre":"laura","edad": 20,"nota":4.5}
# estudiantes["curso"]= "programacion"
# print(estudiantes)

# estudiantes={"nombre":"laura","edad": 20,"nota":4.5}
# del estudiantes["edad"]
# print(estudiantes)

# estudiante={"nombre":"laura","edad": 20,"nota":4.5}
# estudiante.clear()
# print(estudiante)

# estudiante={"nombre":"laura","edad": 20,"nota":4.5}
# for clave in estudiante:
#     print(clave)

# estudiante={"nombre":"laura","edad": 20,"nota":4.5}
# for clave, valor in estudiante.items():
#     print(f"{clave}:{valor}")

# estudiante={"nombre":"laura","edad": 20,"nota":4.5}
# for valor in estudiante.values():
#     print(valor)

# frutas={"manzana","pera","banano"}
# print(frutas)

# numeros={1,2,3,3,4,5}
# print(numeros)

# colores={"rojo","azul"}
# colores.add("verde")
# print(colores)

# colores={"rojo","azul"}
# colores.remove("azul")
# print(colores)

# colores={"rojo","azul","verde"}
# colores.discard("rojo")
# print(colores)

# colores={"rojo","azul","verde"}
# colores.remove("negro")
# print(colores)

# colores={"rojo","azul","verde"}
# colores.discard("negro")
# print(colores)

# A={"rojo","verde","azul",}
# B={"amarillo","verde","negro"}
# union= A | B
# print(union)

# A={"rojo","verde","azul",}
# B={"amarillo","verde","negro"}
# union= A.union(B)
# print(union)

# A={"rojo","verde","azul",}
# B={"amarillo","verde","negro"}
# inter= A & B
# print(inter)

# A={"rojo","verde","azul",}
# B={"amarillo","verde","negro"}
# inter =A.intersection(B)
# print(inter)

# A={"rojo","verde","azul",}
# B={"amarillo","verde","negro"}
# diferencia= A - B
# print(diferencia)

# A={"rojo","verde","azul",}
# B={"amarillo","verde","negro"}
# dif_sim=A^B
# print(dif_sim)

# A={"rojo","verde","azul",}
# B={"amarillo","verde","negro"}
# dif_sim= A.symmetric_difference(B)
# print(dif_sim)

# ARCHIVOS

# archivo= open("ejemplo.txt","w")
# archivo.write("Mi nombnre es\n")
# archivo.write("Brayan Uriel\n")
# archivo.close()

#archivo agregar otra linea de datos

# archivo= open("ejemplo.txt","a")
# contenido=archivo.write("Nuevalinea agregada\n")
# archivo.close()

#leer archivo

# archivo= open("ejemplo.txt","r")
# contenido=archivo.read()
# print(contenido)
# archivo.close()

# with open

# with open("notas.txt","a") as archivo:
#     archivo.write("nueva linea agregada\n")

# insertar y guardar

# with open("estudiantes.txt","w") as ejemplo:
#     for i in range(3):
#         nombre= input("ingresa del nombre del estudiante:")
#         ejemplo.write(nombre +"\n")
        
# with open("estudiantes.txt","r") as ejemplo:
#     print("\n lista de estudiantes graduados:")
#     print(ejemplo.read())

# vaciar un archivo

# with open("estudiantes.txt","w")as archivo:
#     pass