
cliente={}
op=""

while op !=4:
    if op ==1:
        identificasion=input("digite su identificasion: ")
        nombre=input("escriba su nombre: ")
        direccion=input("escriba su dereccion: ")
        telefono=("digite su telefono: ")
        correo=input("digite su correo ")
        empresa=input("escriba el nombre de su empresa: ")
        cliente={
            "identificasion":identificasion,
            "nombre":nombre,
            "direccion":direccion,
            "telefono":telefono,
            "correo":correo,
            "empresa":empresa
        }
    if op ==2:
        print("-----------------------")
        print("<<<informacion del cliente>>>")
        print("------------------------")
        print("identificasion:" , cliente["identificasion"])
        print("nombre completo:",cliente ["nombre"])
        print("direccion:",cliente ["direccion"])
        print("telefono:",cliente ["telefono"])
        print("correo:",cliente ["correo"])
        print("empresa:",cliente ["empresa"])

    if op ==3:

        del [identificasion]
        print(">>>-----------------------<<<")
        print("ciente eliminado con exito !")

    if op ==4:
        exit
    print("---MENU---")
    print("1---AÑADIR CLIENTE---")
    print("2-MOSTRAR CLIENTE")
    print("3-ELIMINAR CLNETE")
    print("4-.SALIR")
    op=int(input("digite la opcion seleccionada: "))   
