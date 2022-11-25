
factura=[]
codigoclient=[]
nombreclient=[]
fechfactura=[]
producto=[]
precio=[]
cantidad=[]
total=[]

tamaño=int(input("tamaño de la lista?: "))

for i in range(tamaño):

    print("ingrese los datos de facturacion" ,i+1)
    facturas=input("codigo de factura: ")
    codigoclientes= input("codigo del cliente: ")
    nombreclients =input("nombre del cliente: ")
    fechfacturas =input("fecha de la factura: ")
    precios =input("ingrese los precios: ")
    cantidad =("cantidad de precios: ")
    totales =("tatal de la factura: ")

    factura.append(facturas)
    codigoclient.append(codigoclientes)
    nombreclient.append(nombreclients)
    fechfactura.append(fechfacturas)
    precio.append(precios)
    cantidad.append(cantidad)
    total.append(totales)


for i in range(tamaño):
    
    print("--------------------------------")
    print("--------------------------------")
