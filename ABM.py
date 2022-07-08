import os
from consultas import Consultas
from imagenes import img
from listados import Listados
from registracion import reg


class Abm():

    def __init__(self):
        pass

    def usuario(self):
        while True:
            img.abm_usuarios()
            print('Opcion 1: Listar Usuarios')
            print('Opcion 2: Registrar Usuarios')
            print('Opcion 3: Modificar el telefono de un usuario.')
            print('Opcion 4: Modificar el sector de un usuario.')
            print('Opcion 5: Dar de baja un usuario.')
            print('Opcion 6: Volver al menu principal.')
            opcion = int(input('Elija una de las opciones:\n'))
            #os.system('cls')
            if opcion == 1:
                os.system('cls')
                Listados().usuarios()
            elif opcion == 2:
                reg.registracion_usuario()
            elif opcion == 3:
                Listados().usuarios()
                unUsuario = int(input("Ingrese el ID del usuario que quiere modificar:\n"))
                unTelefono = input("Ingrese el nuevo numero:\n")
                Consultas().update_sectorUsuario(unUsuario, unTelefono)
            elif opcion == 4:
                Listados().usuarios()
                unUsuario = int(input("Ingrese el ID del usuario que quiere modificar:\n"))
                Listados().sectores()
                unSector = int(input("Ingrese el ID del nuevo sector:\n"))
                Consultas().update_sectorUsuario(unUsuario, unSector)
            elif opcion == 5:
                Listados().usuarios()
                unUsuario = int(input("Ingrese el ID del usuario que quiere ELIMINAR:\n"))
                Consultas().eliminar_usuario(unUsuario)
            elif opcion == 6:
                break

    def producto(self):
        while True:
            img.abm_productos()
            print('Opcion 1: Listar productos.')
            print('Opcion 2: registrar producto.')
            print('Opcion 3: eliminar producto.')
            print('Opcion 4: Volver al menu principal')
            opcion = int(input('Elija una de las opciones:\n'))
            # os.system('cls')
            if opcion == 1:
                Listados().productos()
            elif opcion == 2:
                print("primero ingrese la factura!")
                fact = reg.registracion_factura()
                cantidad = int(input("Ingrese la cantidad de productos que va registrar con esta factura:\n"))
                for i in range(cantidad):
                    reg.registracion_producto(fact)
            elif opcion == 3:
                unProducto = int(input("Ingrese el ID del producto que quiere ELIMINAR:\n"))
                Consultas().eliminar_producto(unProducto)
            elif opcion == 4:
                break

    def proveedor(self):
        while True:
            img.abm_proveedores()
            print('Opcion 1: Listar proveedores.')
            print('Opcion 2: Registrar proveedor.')
            print('Opcion 3: Modificar la direccion de un proveedor.')
            print('Opcion 4: Modificar el telefono de un proveedor')
            print('Opcion 5: Dar de baja un proveedor.')
            print('Opcion 6: Volver al menu principal.')
            opcion = int(input('Elija una de las siguientes opciones:\n'))
            if opcion == 1:
                Listados().proveedores()
            elif opcion == 2:
                reg.registracion_proveedor()
            elif opcion == 3:
                Listados().proveedores()
                unProveedor = int(input("Ingrese el ID del proveedor que quiere modificar:\n"))
                unaDireccion = input("Ingrese la nueva direccion:\n")
                Consultas().update_direccionProveedor(unProveedor, unaDireccion)
            elif opcion == 4:
                Listados().proveedores()
                unProveedor = int(input("Ingrese el ID del proveedor que quiere modificar:\n"))
                unTelefono = input("Ingrese el nuevo numero:\n")
                Consultas().update_direccionProveedor(unProveedor, unTelefono)
            elif opcion == 5:
                Consultas.eliminar_proveedor()
            elif opcion == 6:
                break

    def asignacion(self):
        while True:
            img.abm_asignaciones()
            print('Opcion 1: Listar Asignaciones')
            print('Opcion 2: Alta asignacion')
            print('Opcion 3: Baja asignacion')
            print('Opcion 4: Volver al menu principal')
            opcion = int(input("ingrese la opcion:\n"))
            #os.system('cls')
            if opcion == 1:
                Listados().asignaciones()
            elif opcion == 2:
                reg.asignaciones()
            elif opcion == 3:
                Listados().asignaciones()
                unaAsignacion = int(input("Ingrese el ID de la asignacion que quiere ELIMINAR:\n"))
                Consultas().eliminar_asignacion(unaAsignacion)
            elif opcion == 4:
                break

    def ticket(self, adm):
        while True:
            img.abm_ticket()
            print('Opcion 1: Listar mis tickets.')
            print('Opcion 2: Registrar ticket.')
            print('Opcion 3: cambiar estado de un ticket.')
            print('Opcion 4: Cambiar prioridad.')
            print('Opcion 5: Volver al menu principal')
            opcion = int(input("ingrese la opcion:\n"))
            os.system('cls')
            if opcion == 1:
                Listados().tickets(adm.get_id())
            elif opcion == 2:
                reg.registrar_ticket(adm)
            elif opcion == 3:
                Listados().tickets(adm.get_id())
                unTicket = input("Ingrese el ID del ticket:\n")
                unEstado = input('5- Cerrado \n4- En Testeo.\n3- Resuelto.\n2- En Curso.\n1- Nuevo.\nIngrese el estado:\n')
                Consultas().update_estadoTicket(unTicket, unEstado)
            elif opcion == 3:
                Listados().tickets(adm.get_id())
                unTicket = int(input("Ingrese el ID del ticket:\n"))
                unaPrioridad = int(input('4- Urgente.\n3- Alta.\n2- normal.\n1 -baja.\nIngrese la prioridad:\n'))
                Consultas().update_prioridadTicket(unTicket, unaPrioridad)
            elif opcion == 5:
                break


abm = Abm()
