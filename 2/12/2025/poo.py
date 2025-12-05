class Persona:
    def _init_(self,nombre,edad):
        self.nombre= nombre
        self.edad= edad
        
def saludar(self):
    print(f"hola, soy {self.nombre} y tengo {self. edad} años.")
    
persona1 = Persona("laura",20)
peesona2 = Persona("andres",25)

persona1.saludar()
peesona2.saludar()