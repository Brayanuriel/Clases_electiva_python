# with open("agenda_Brayan_Vasquez.txt","w") as ejemplo:
#      for i in range(6):
#         nombre= input("ingrese el nombre :")
#         telefono=input("ingrese el telfono:")
#         direccion=input("ingrese la direccion:")
#         ejemplo.write(nombre + "," + telefono + "," + direccion +"\n")
         
# with open("agenda_Brayan_vasquez.txt","r") as ejemplo:
#      print("\n personas registradas en la agenda:")
#      print(ejemplo.read())
     
def registrar_personas(archivo, cantidad=6):
     with open(archivo, "w") as ejemplo:
          for _ in range(cantidad):
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            direccion = input("Ingrese la dirección: ")
            ejemplo.write(f"{nombre},{telefono},{direccion}\n")
