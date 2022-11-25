nombres=[]
identificasion=[]
celular=[]
correo=[]
direccion=[]
fecha=[]
lugar=[]

tamaño=int(input("tamaño de la lista?: "))

for i in range (tamaño):
    print("ingrese los datos del aprendiz", i+1)
    nombre=input("nombre del aprendiz: ")
    id = input("A de identificasion: ")
    cel=input("digite el telefono: ")
    corr=input("digite el correo: ")
    fech=("digite la fecha: ")
    lug=("digite el lugar: ")

    nombres.append(nombre)
    identificasion.append(id)
    celular.append(cel)
    correo.append(corr)
    fecha.append(fech)
    lugar.append(lug)
    
print("lo apremdices son: ")
for i in range(tamaño):
    print("--------------------------------")
    print("--------------------------------")
    print("nombre: ", nombres[i])
    print("identificasion: ", identificasion[i])
    print("numero de telefono: ",celular[i])
    print("correo electronico: ", correo[i])
    