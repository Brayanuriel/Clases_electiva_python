def registrar_personas(archivo, cantidad=6):
     with open(archivo, "w") as ejemplo:
          for _ in range(cantidad):
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            direccion = input("Ingrese la dirección: ")
            ejemplo.write(f"{nombre},{telefono},{direccion}\n")

def mostrar_personas(archivo):
    print("\nPersonas registradas en la agenda:")
    with open(archivo, "r") as ejemplo:
        print(ejemplo.read())


def inicio():
    archivo = "agenda_Brayan_Vasquez.txt"
    registrar_personas(archivo)
    mostrar_personas(archivo)


inicio()  