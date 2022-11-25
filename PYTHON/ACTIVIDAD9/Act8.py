#App que diseñe ye almacne los datos de un vehiculo,para ello debe crear las siguientes listas vacias alimentarlas y mostrarlas por pantalla

marca=[]
modelo=[]
color=[]
combustible=[]
precio=[]

tamaño=int(input("tamaño de la lista?: "))

for i in range(tamaño):
    print("ingrese la marca del vehiculo" ,i+1)
    marcas=input("marca del vehiculo: ")
    modelos = input("modelo del vehiculo: ")
    colores =input("digite el color: ")
    combustibles =input("digite el combustible: ")
    precios =input("precio del vehiculo: ")

    marca.append(marcas)
    modelo.append(modelos)
    color.append(colores)
    combustible.append(combustibles)
    precio.append(precios)


for i in range(tamaño):
    print("--------------------------------")
    print("--------------------------------")
