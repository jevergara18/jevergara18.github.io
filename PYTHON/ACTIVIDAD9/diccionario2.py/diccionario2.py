#diseñe una app que permita al usuario nombre,edad,direccion,y telefono;estos datos se deben almacnar en un diccionario llamado persona.
#estos datos se pueden mostrar por pantalla de forma concatenada 

#ejemplo: juan tiene 17 años vive en la calle 8 27 18a y su numero de telefono es 1234567


nombre=input ("Digite su nobre: ")
edad=input("Digite su Edad: ")
direcion=input("Digite su dirrecion: ")
telefono=input("Digite su telefono: ")

persona={"nombre":nombre,"edad":edad,"dirrecion":direcion,"telefono":telefono}

print(persona["nombre"],"tiene: ",persona["edad"],"años",",y vive en: ", persona["direccion"],"y su numero de telefono es: ",persona["telefono"])