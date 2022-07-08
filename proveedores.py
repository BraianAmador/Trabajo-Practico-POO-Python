from mySql import dba


class Proveedor():
    def __init__(self, nombre, direccion, telefono, localidad):
        self.__ids = 0
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__localidad = localidad

    def get_id(self):
        return self.__ids

    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono

    def get_localidad(self):
        return self.__localidad

    def set_id(self, ids):
        self.__ids = ids

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_localidad(self, localidad):
        self.__localidad = localidad

    def save(self):
        sql = 'insert into proveedores (nombre, direccion, telefono, localidad) values(%s,%s,%s,%s)'
        val = (self.get_nombre(), self.get_direccion(), self.get_telefono(), self.get_localidad())
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
