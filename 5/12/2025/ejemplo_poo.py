class Estudiante:
    def __init__(self,nombre,notas):
        self.nombre = nombre
        self.notas = notas
        
        
    def calcular_promedio(self):
        promedio = sum(self.notas) / len(self.notas)
        return promedio
    
    
    def mostrar_info(self):
        promedio = self.calcular_promedio()
        if promedio>=3.0:
            estado="aprobado"
        else:
            estado="reprobado"
        print(f"\n el promedio de las notas de{self.nombre}es:{promedio:.2f},por esto el estudiante esta ({estado})")
            
        
lista_estudiantes =[]
cantidad = int(input("cuantos estudiantes debe registrar:"))

for i in range(cantidad):
    print(f"\n estudiantes numero {i+1}")
    nombre = input("nombre:")
    notas = []
        
    for i in range(3):
        nota = float(input(f"ingrese la nota numero {i+1} de {nombre}:"))
        notas.append(nota)
            
estudiante = Estudiante (nombre,notas)
lista_estudiantes.append(estudiante)
            
aprobados = 0

for est in lista_estudiantes:
    est.mostrar_info()
    if est.calcular_promedio()>= 3.0:
        aprobados +=1
            
print(f"\n entonces de los {cantidad} estudiantes")
print(f"\n{aprobados}aprobaron")
print(f"{len(lista_estudiantes)-aprobados} reprobaron")