from administrador import Administrador
from asignaciones import Asignacion
from facturas import Factura
from marcas import Marca
from proveedores import Proveedor
from sectores import Sector
from usuarios import Usuario
from validator import val
from tickets import Ticket
from listados import Listados
from productos import Producto
from imagenes import img


class Registracion():

    def __init__(self):
        pass

    def registracion_usuario(self):
        img.registrar_usuario()
        i = False
        while not i == True:
            usuario = {}
            usuario['nombre'] = input('ingrese nombre:\n')
            usuario['apellido'] = input('ingrese apellido:\n')
            usuario['telefono'] = input('ingrese telefono:\n')
            Listados().sectores()
            usuario['codigoSector'] = input('ingrese sector:\n')
            errores = val.validar_usuario(usuario)
            if not errores:
                cargarUsuario = Usuario(**usuario)
                cargarUsuario.save()
                print("Se cargo el usuario correctamente!")
                i = True
                return cargarUsuario
            for i in errores.values():
                print(i)

    def registracion_factura(self):
        img.registrar_factura()
        i = False
        while not i == True:
            factura = {}
            factura['numero'] = input('ingrese numero:\n')
            factura['fechaDeCompra'] = input('ingrese fecha de compra(YYYY-mm-dd):\n')
            Listados().proveedores()
            factura['codigoProveedor'] = input('ingrese el ID del proveedor:\n')
            errores = val.validar_factura(factura)
            if not errores:
                cargarFactura = Factura(**factura)
                cargarFactura.save()
                print("Se cargo la factura correctamente!")
                i = True
                return cargarFactura
            for i in errores.values():
                print(i)

    def registracion_marca(self):
        img.registrar_marca()
        i = False
        while not i == True:
            marca = {'nombre': input('ingrese nombre: ')}
            errores = val.validar_marca(marca)
            if not errores:
                cargarMarca = Marca(**marca)
                cargarMarca.save()
                print("Se cargo la marca correctamente!")
                i = True
                return cargarMarca
            for i in errores.values():
                print(i)

    def registracion_proveedor(self):
        img.registrar_proveedor()
        i = False
        while not i == True:
            proveedor = {}
            proveedor['nombre'] = input('ingrese nombre: ')
            proveedor['direccion'] = input('ingrese direccion: ')
            proveedor['telefono'] = input('ingrese telefono: ')
            proveedor['localidad'] = input('ingrese localidad: ')
            errores = val.validar_proveedor(proveedor)
            if not errores:
                cargarProveedor = Proveedor(**proveedor)
                cargarProveedor.save()
                print("Se cargo el proveedor correctamente!")
                i = True
                return cargarProveedor
            for i in errores.values():
                print(i)

    def registracion_sector(self):
        img.registrar_sector()
        i = False
        while not i == True:
            sector = {'nombre': input('ingrese nombre: ')}
            errores = val.validar_sector(sector)
            if not errores:
                cargarSector = Sector(**sector)
                cargarSector.save()
                print("Se cargo el sector correctamente!")
                i = True
                return cargarSector
            for i in errores.values():
                print(i)

    def registracion_asignacion(self):
        img.registrar_asignacion()
        i = False
        while not i == True:
            asignar = {}
            Listados().productos()
            asignar['codigoProducto'] = int(input('ingrese producto:\n'))
            Listados().usuarios()
            asignar['codigoUsuario'] = int(input('ingrese usuario:\n'))
            errores = val.validar_asignacion(asignar)
            if not errores:
                cargarAsignacion = Asignacion(**asignar)
                cargarAsignacion.save()
                print("Se cargo la asignacion correctamente!")
                i = True
                return cargarAsignacion
            for i in errores.values():
                print(i)

    def registracion_administrador(self):
        img.registrar_administrador()
        i = False
        while not i == True:
            administrador = {
                'nombre': input('ingrese su nombre:\n'),
                'apellido': input('ingrese su apellido:\n'),
                'mail': input('ingrese su mail:\n'),
                'interno': input('ingrese su numero de interno:\n'),
                'password': input("Ingrese una clave Que contenga una minuscula,una mayuscula y un caracter especial @ # $ %:\n"),
                'cpassword': input("Confirme la clave:\n")
            }
            errores = val.validar_administrador(administrador)
            if not errores:
                administrador.pop('cpassword')
                cargarAdmin = Administrador(**administrador)
                cargarAdmin.save()
                print("Se registro correctamente!")
                i = True
                return cargarAdmin
            for i in errores.values():
                print(i)

    def registrar_ticket(self, administrador):
        img.registrar_ticket()
        i = False
        while not i == True:
            ticket = {
                'titulo': input(f'{("-" * 45)}\nIngrese el titulo:\n'),
                'descripcion': input(f'{("-" * 45)}\nIngrese una descripcion:\n'),
                'prioridad': input(f'{("-" * 45)}\n4- Urgente.\n3- Alta.\n2- normal.\n1 -baja.\nIngrese numero de la prioridad:\n'),
                'estado': input(f'{("-" * 45)}\n5- Cerrado \n4- En Testeo.\n3- Resuelto.\n2- En Curso.\n1- Nuevo.\nIngrese el estado:\n'),
            }
            errores = val.validar_ticket(ticket)
            if not errores:
                ticket['administrador'] = administrador
                ticket1 = Ticket(**ticket)
                ticket1.save()
                print('Se genero con exito el ticket')
                return ticket1
            for i in errores.values():
                print(i)

    def registracion_producto(self, factura):
        img.registrar_producto()
        i = False
        while not i == True:
            producto = {}
            producto['descripcion']: input('ingrese nombre: ')
            opcion = int(input("Si la marca no se encuentra en la lista oprima 0(cero) para registrarla de lo contrario oprima 1."))
            if opcion == 0:
                laMarca = self.registracion_marca()
                print(f'se registro la marca, el numero de id es {laMarca.get_id()}.')
                producto['codigoMarca']: laMarca.get_id()
            else:
                producto['codigoMarca']: input('ingrese el ID de la marca: ')
            producto['modelo']: input('ingrese el modelo: ')
            producto['precio']: input('ingrese el precio: ')
            errores = val.validar_producto(producto)
            if not errores:
                producto[factura] = factura
                producto1 = Producto(**producto)
                producto1.save()
                print("Se cargo el producto correctamente!")
                i = True
                return producto1
            for i in errores.values():
                print(i)


reg = Registracion()
