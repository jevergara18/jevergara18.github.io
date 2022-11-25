// "39.diseñe un algoritmo que muestre un menu donde las operaciones sean 
//1.suma
//2.resta
//3.division
//4.muliplicasion"

var op;

var n1,n2, resultado;

op=parseInt(prompt("escogja una opcion :1.suma 2.resta 3.division 4.multiplicacin"))

switch(op){
    case 1:
        n1=parseInt(prompt("digite el primer numero: "))
        n2=parseInt(prompt("digite el segundo numero: "))
        resultado=n1+n2;
        document.write("la suma de:" +n1+ "+" +n2+ "es:" +resultado)
    
    break;
    case 2:
        
        nn1=parseInt(prompt("digite el primer numero: "))
        n2=parseInt(prompt)("digite el segundo numero: ")
        resultado=n1-n2;
        document.write("la resta de:" +n1+ "-" +n2+ "es:" +resultado)

    break;
    case 3:

        n1=parseInt(prompt("digite el primer numero: "))
        n2=parseInt(prompt("digite el segundo numero: "))
        resultado=n1*n2;
        document.write("la multiplicacion de:" +n1+ "*" +n2+ "es:" +resultado)

    break;
    case 4:

        n1=parseInt(prompt("digite el primer numero: "))
        n2=parseFloat(prompt("digite el segundo numero: "))
        resultado=n1/n2;
        document.write("la division de:" +n1+ "/" +n2+ "es:" +resultado)



}