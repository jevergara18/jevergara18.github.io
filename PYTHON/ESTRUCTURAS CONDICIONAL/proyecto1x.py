"""evaluar la edad ingresada
0>= y <2, eres un baby
2>=y <12, eres un niño (a)
12>=y <=17, eres un adolecente
10>= y <40, eres un adulto joven 
40>= y <60, eres un adulto maduro
>=60, eres un adulto mayor
"""

n=int(input("ingrese la edad "))

if n>0 and n<2:
    print("eres un baby")
elif n>2 and n<12:
    print("eres un niñ@")
elif n>12 and n<17:
    print("eres un adolecente")
elif n>18 and n<40:
    print("eres un adulto joven")
elif n>40 and n<60:
    print("eres un adulto maduro")
elif n>60
    print("eres un adulto mayor")
else:
    print("digite su edad correctamnete")

 