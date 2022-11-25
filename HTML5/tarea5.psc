Algoritmo  tarea5
	Definir i Como Entero
	
	Escribir "los numeros primos del 1 al 100 son:"
	Escribir "_____________________________________"
	
	Definir x, num, contador Como Entero
	para num <- 1 Hasta 100 hacer 
		x=1
		contador =0
		mientras x <= num Hacer
			si num mod x = 0 Entonces
				contador = contador + 1 
				
			FinSi
			x=x+1
		FinMientras
		si contador ==2 Entonces
			Escribir "el numero ",num," es primo"
		FinSi
	FinPara
