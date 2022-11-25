#app que al ingresar el valor de compra 
#si el valor de la compra es mayor 1000.000
#entonces calcule el descuento (7%)y total de la compra
valor_compra=float(input("digite el valor de la compra"))

if valor_compra>100000:
    descuento=valor_compra*0.07
    total=valor_compra-descuento
    print("subtotal:",valor_compra,)
    print("descuento:",descuento,)
    print("total de compra:",total,)

else:  
    descuento=valor_compra*0.0
    total=valor_compra-descuento
    print("subtotal:",valor_compra,)
    print("descuento:",descuento,)
    print("total de compra:",total,)
