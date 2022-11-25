function sumar (){
    var x,y,z
    x=document.getElementById("n1").value
    y=document.getElementById("n2").value
    z=parseInt(x)+parseInt(y)

    document.getElementById("resultado_suma").innerHTML= "la suma es:"+z
}

function restar (){
    var x,y,z
    x=document.getElementById("n1").value
    y=document.getElementById("n2").value
    z=parseInt(x)-parseInt(y)

    document.getElementById("resultado_resta").innerHTML= "la resta es:"+z
}

    function multiplicar(){
        var x,y,z
        x=document.getElementById("n1").value
        y=document.getElementById("n2").value
        z=parseInt(x)*parseInt(y)
    
        document.getElementById("resultado_multiplicacion").innerHTML= "la multplicacion es:"+z
    }

    function dividir (){
        var x,y,z
        x=document.getElementById("n1").value
        y=document.getElementById("n2").value
        z=parseInt(x)/parseInt(y)
    
        document.getElementById("resultado_division").innerHTML= "la division es:"+z
    }