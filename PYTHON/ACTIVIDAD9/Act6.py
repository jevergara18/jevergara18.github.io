
nombres=[]
identificasion=[]
tamaño=int(input("tamaño de la lista?: "))

for i in range (tamaño):
    print("ingrese los datos del aprendiz", i+1)
    nombre=input("nombre del aprendiz: ")
    id = input("A de identificasion: ")
    nombres.append(nombre)
    identificasion.append(id)
print("lo apremdices son: ")
for i in range(tamaño):
    print("--------------------------------")
    print("nombre: ", nombres[i])
    print("identificasion: ", identificasion[i])