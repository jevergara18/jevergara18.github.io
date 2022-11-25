#app que la ingresar la temperatura del paciente diga si tiene fiebre o no 
n=int(input("digite la temperatura:"))

if n>38:
    print("la temperatura de",n,"es positivo para fiebre")
else:
    print("el paciente con la temperatura",n," tiene la temperatura normal")
