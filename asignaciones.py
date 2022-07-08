from mySql import dba


class Asignacion():
    def __init__(self, codigoProducto, codigoUsuario):
        self.__ids = 0
        self.__codigoProducto = codigoProducto
        self.__codigoUsuario = codigoUsuario

    def get_id(self):
        return self.__ids

    def get_codigoProducto(self):
        return self.__codigoProducto

    def get_codigoUsuario(self):
        return self.__codigoUsuario

    def set_id(self, ids):
        self.__ids = ids

    def set_codigoProducto(self, codigoProducto):
        self.__codigoProducto = codigoProducto

    def set_codigoUsuario(self, codigoUsuario):
        self.__codigoUsuario = codigoUsuario

    def save(self):
        sql = 'insert into asignaciones (producto_id, usuario_id) values(%s,%s)'
        val = (self.get_codigoProducto(), self.get_codigoUsuario())
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
