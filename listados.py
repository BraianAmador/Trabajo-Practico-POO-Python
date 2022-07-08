from mySql import dba


class Listados():

    def __init__(self):
        pass

    def asignaciones(self):
        print("+----------+--------------------+----------+--------------------+")
        print("|  usr_id  |      Usuario       |  prod_id |      Productos     |")
        print("+----------+--------------------+----------+--------------------+")
        dba.get_cursor().execute('select * from productosasignados')
        for i in dba.get_cursor().fetchall():
            usuario_id = i[0]
            usuario = i[1]
            producto_id = i[2]
            producto = i[3]
            cadena = "|{:>10}|{:>20}|{:>10}|{:>20}|".format(usuario_id, usuario, producto_id, producto)
            print(cadena)
            print("+----------+--------------------+----------+--------------------+")

    def usuarios(self):
        print("+----------+--------------------+--------------------+--------------------+")
        print("|    id    |       Usuario      |      Telefono      |       Sector       |")
        print("+----------+--------------------+--------------------+--------------------+")
        dba.get_cursor().execute('SELECT * from listausuarios')
        for i in dba.get_cursor().fetchall():
            usuario_id = i[0]
            usuario = i[1]
            telefono = i[2]
            sector = i[3]
            cadena = "|{:>10}|{:>20}|{:>20}|{:>20}|".format(usuario_id, usuario, telefono, sector)
            print(cadena)
            print("+----------+--------------------+--------------------+--------------------+")

    def productos(self):
        print("+----------+--------------------+---------------+------------------------------+")
        print("|    id    |      Produtos      |     Marca     |           Modelo             |")
        print("+----------+--------------------+---------------+------------------------------+")
        dba.get_cursor().execute('select * from listaproductos')
        for i in dba.get_cursor().fetchall():
            producto_id = i[0]
            producto = i[1]
            marca = i[2]
            modelo = i[3]
            cadena = "|{:>10}|{:>20}|{:>15}|{:>30}|".format(producto_id, producto, marca, modelo)
            print(cadena)
            print("+----------+--------------------+---------------+------------------------------+")

    def marcas(self):
        print("+----------+--------------------+")
        print("|    id    |        Marca       |")
        print("+----------+--------------------+")
        dba.get_cursor().execute('select * from marcas')
        for i in dba.get_cursor().fetchall():
            marca_id = i[0]
            nombre = i[1]
            cadena = "|{:>10}|{:>20}|".format(marca_id, nombre)
            print(cadena)
            print("+----------+--------------------+")

    def sectores(self):
        print("+----------+--------------------+")
        print("|    id    |       Sector       |")
        print("+----------+--------------------+")
        dba.get_cursor().execute('select * from sectores')
        for i in dba.get_cursor().fetchall():
            sector_id = i[0]
            nombre = i[1]
            cadena = "|{:>10}|{:>20}|".format(sector_id, nombre)
            print(cadena)
            print("+----------+--------------------+")

    def proveedores(self):
        print("+------+---------------+------------------------------+---------------+--------------------+")
        print("|  id  |   Proveedor   |          Direccion           |   telefono    |     Localidad      |")
        print("+------+---------------+------------------------------+---------------+--------------------+")
        dba.get_cursor().execute('select * from proveedores')
        for i in dba.get_cursor().fetchall():
            proveedor_id = i[0]
            nombre = i[1]
            direccion = i[2]
            telefono = i[3]
            localidad = i[4]
            cadena = "|{:>6}|{:>15}|{:>30}|{:>15}|{:>20}|".format(proveedor_id, nombre, direccion, telefono, localidad)
            print(cadena)
            print("+------+---------------+------------------------------+---------------+--------------------+")

    def tickets(self, idAdm):
        print("P = Prioridad(4- Urgente. * 3- Alta. * 2- normal. * 1 -baja.")
        print("E = Estado(5- Cerrado * 4- En Testeo. * 3- Resuelto. * 2- En Curso. * 1- Nuevo.")
        print("+------+-------------------------+--------------------------------------------------+-----+-----+")
        print("|  id  |         Titulo          |                   Descripcion                    |  P  |  E  |")
        print("+------+-------------------------+--------------------------------------------------+-----+-----+")
        sql = 'select * from tickets where administrador_id=%s'
        val = (idAdm,)
        dba.get_cursor().execute(sql, val)
        for i in dba.get_cursor().fetchall():
            ticket_id = i[0]
            titulo = i[1]
            descripcion = i[2]
            prioridad = i[3]
            estado = i[4]
            cadena = "|{:>6}|{:>25}|{:>50}|{:>5}|{:>5}|".format(ticket_id, titulo, descripcion, prioridad, estado)
            print(cadena)
            print("+------+-------------------------+--------------------------------------------------+-----+-----+")
