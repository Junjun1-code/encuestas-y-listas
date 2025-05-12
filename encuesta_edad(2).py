edades=[]
lugares=[]
area=[]
for i in range(int(input("¿Cuantos estudiantes seran encuestados?"))):
    lugares.append(input("Lugar de encuesta: "))
    edades.append(int(input("¿Cual es su edad?: ")))
    area.append(input("¿Cual es su carrera?: "))

for i in range(len(edades)):
    if edades[i]==min(edades):
        print(f"{min(edades)} es la edad minima, encuestado en {lugares[i]} y ubicacion en la tabla {edades.index(min(edades))+1}")
        break

print (f"{max(edades)} es la edad más alta")
print (f"{sum(edades)/len(edades)} es el promedio de edades")

cont=0
for i in edades:
    if i>(sum(edades)/len(edades)):
        cont+=1

print (f"{cont} estudiantes superan el promedio de edades")

cont=0
for i in area:
    if i.lower()=="informatica":
        cont+=1

print (f"{cont} estudiantes son del area de informatica")
