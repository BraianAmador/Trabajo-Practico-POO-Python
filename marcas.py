from mySql import dba


class Marca():
    def __init__(self, nombre):
        self.__ids = 0
        self.__nombre = nombre

    def get_id(self):
        return self.__ids

    def get_nombre(self):
        return self.__nombre

    def set_id(self, ids):
        self.__ids = ids

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def save(self):
        sql = 'insert into marcas(nombre) values(%s)'
        val = (self.get_nombre(),)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
