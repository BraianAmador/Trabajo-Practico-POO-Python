from mySql import dba


class Usuario():

    def __init__(self, nombre, apellido, telefono, codigoSector):
        self.__ids = 0
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__codigoSector = codigoSector

    def get_id(self):
        return self.__ids

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_telefono(self):
        return self.__telefono

    def get_codigoSector(self):
        return self.__codigoSector

    def set_id(self, ids):
        self.__ids = ids

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_codigoSector(self, codigoSector):
        self.__codigoSector = codigoSector

    def save(self):
        sql = 'insert into usuarios (nombre, apellido, telefono, sector_id) values(%s,%s,%s,%s)'
        val = (self.get_nombre(), self.get_apellido(), self.get_telefono(), self.get_codigoSector())
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)


