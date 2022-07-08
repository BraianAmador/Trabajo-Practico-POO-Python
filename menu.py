import os
import stdiomask
from ABM import abm
from administrador import Administrador
from consultas import Consultas
from imagenes import img
from validator import val


class Menu():

    def __init__(self):
        pass

    def login(self):

        login = {
            'mail': input('ingrese su email: '),
            'password': stdiomask.getpass(prompt='ingresar contraseña: ', mask='*')
        }
        mail = login['mail']
        errores = val.validar_login(login)

        return errores, mail

    def miMenu(self, adm):
        bandera = True
        while bandera:
            img.miMenu()
            print('Opcion 1: Modificar mi mail.')
            print('Opcion 2: Modificar mi interno.')
            print('Opcion 3: Modificar mi contraseña.')
            print('Opcion 4: Darme de baja del sistema.')
            print('Opcion 5: Generar ticket.')
            print('Opcion 6: Menu Alta, bajas y modificaciones de equipos y usuarios.')
            print('Opcion 7: Logout')
            opcion = int(input("ingrese una opcion:\n"))
            if opcion == 1:
                print(f"Su mail actual es {adm.get_mail()}")
                mail = input("Ingrese el nuevo mail:\n")
                adm.update_mail(mail)
                os.system('cls')
                print("se modifico correctamente su mail")
            elif opcion == 2:
                print(f"Su interno actual es {adm.get_interno()}")
                interno = input("ingrese el interno: \n")
                adm.update_interno(interno)
                os.system('cls')
                print("se modifico correctamente su interno")
            elif opcion == 3:
                password = input("ingrese la nueva contraseña: \n")
                adm.update_password(adm.encriptarPass(password))
                os.system('cls')
                print("Se modifico correctamente su contraseña!")
                print("Ingrese con su nueva clave al sistema")
                self.menuLogueado()
            elif opcion == 4:
                adm.delete()
                os.system('cls')
                self.menuLogueado()
            elif opcion == 5:
                os.system('cls')
                abm.ticket(adm)
            elif opcion == 6:
                self.menuABM()
            elif opcion == 7:
                bandera = False
            else:
                img.bonus()

        return bandera

    def menuLogueado(self):
        bandera = True
        while bandera:
            (error, miMail) = self.login()
            if error is None:
                misDatos = Consultas().traer_misDatos(miMail)
                os.system('cls')
                print(f'Bienvenido {misDatos[1]} {misDatos[2]}!')
                adm1 = misDatos[1:]
                adm = Administrador(*adm1)
                adm.set_id(misDatos[0])
                bandera = self.miMenu(adm)
                os.system('cls')
            else:
                for i in error.values():
                    print(f'\n{i}, vuelva a intentarlo.')

    def menuABM(self):
        while True:
            img.menu()
            print('opcion 1: Ingresar ABM usuarios.')
            print('opcion 2: ingresar ABM productos.')
            print('opcion 3: ingresar ABM proveedores.')
            print('opcion 4: ingresar ABM asiganciones.')
            print('opcion 5: Volver al menu principal')
            otraOpcion = int(input('Elija una opcion:\n'))
            os.system('cls')
            if otraOpcion == 1:
                abm.usuario()
            elif otraOpcion == 2:
                abm.producto()
            elif otraOpcion == 3:
                abm.proveedor()
            elif otraOpcion == 4:
                abm.asignacion()
            elif otraOpcion == 5:
                break
            else:
                os.system('cls')
                img.bonus()


menu = Menu()
