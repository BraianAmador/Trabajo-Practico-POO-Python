import os
from menu import menu
from registracion import reg
from imagenes import img

while True:
    os.system('cls')
    img.bienvenido()
    print('opcion 1: Ingresar al sistema')
    print('opcion 2: Registrarse en el sistema')
    print('opcion 3: salir')
    opcion = int(input('Elija una opcion: '))
    # os.system('cls')
    if opcion == 1:
        menu.menuLogueado()
    elif opcion == 2:
        os.system('cls')
        adm = reg.registracion_administrador()
        os.system('cls')
        print(f'Bienvenido {adm.get_nombre()} {adm.get_apellido()}!')
        bandera = menu.miMenu(adm)
    elif opcion == 3:
        img.salida()
        break
    else:
        img.bonus()


