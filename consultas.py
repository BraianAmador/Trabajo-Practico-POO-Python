from mySql import dba


class Consultas():

    def __init__(self):
        pass

    def eliminar_usuario(self, idUser):
        sql = 'call eliminarUsuario(%s)'
        val = (idUser,)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def update_telefonoUsuario(self, telefono, idUsuario):
        sql = 'call modificarTelefonoUsuario(%s, %s)'
        val = (telefono, idUsuario)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def update_sectorUsuario(self, sector, idUsuario):
        sql = 'update usuarios set sector_id=%s where usuario_id=%s'
        val = (sector, idUsuario)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def eliminar_producto(self, idProducto):
        sql = 'delete from productos where producto_id=%s'
        val = (idProducto,)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def eliminar_proveedor(self, idProveedor):
        sql = 'delete from proveedores where proveedor_id=%s'
        val = (idProveedor,)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def update_direccionProveedor(self, direccion, idProveedor):
        sql = 'update proveedores set direccion=%s where proveedor_id=%s '
        val = (direccion, idProveedor)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def update_telefonoProveedor(self, telefono, idProveedor):
        sql = 'update proveedores set telefono=%s where proveedor_id=%s '
        val = (telefono, idProveedor)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def eliminar_asignacion(self, idAsignacion):
        sql = 'delete from asignaciones where asignacion_id=%s'
        val = (idAsignacion,)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def update_estadoTicket(self, estado, idTicket):
        sql = 'update tickets set estado=%s where ticket_id=%s '
        val = (estado, idTicket)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def update_prioridadTicket(self, prioridad, idTicket):
        sql = 'update tickets set prioridad=%s where ticket_id=%s '
        val = (prioridad, idTicket)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def traer_misDatos(self, mail):
        sql = 'select * from administrador where mail=%s'
        val = (mail,)
        dba.get_cursor().execute(sql, val)
        return dba.get_cursor().fetchone()
