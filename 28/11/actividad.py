acumulador=0
for i in range(5):
     numero=float(input(f"ingresa la nota numero {i+1}:"))
     acumulador+=numero
promedio=acumulador/5
print(f"el promedio es : {promedio}")