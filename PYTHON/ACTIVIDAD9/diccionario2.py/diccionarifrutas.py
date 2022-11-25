#diseñe una app que permita el ususraio ingresar frutas y el precio unitario y almacene llamado factura
#despues debe mostrar un mensaje concatenado 
#debe aparecer el nombre de la fruta su valor la cantidad y el total

frutas=input("digite la fruta: ")
precio=int(input("digite el precio"))
cantidad=int(input("digite la cantidad"))

factura={"frutas":frutas,"precio":precio}
print("su",factura["frutas"],"tiene un valor unitario de",factura["precio"],"y su total de la compra es:",(cantidad*precio))