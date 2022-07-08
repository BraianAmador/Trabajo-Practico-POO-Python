from mySql import dba


class Ticket():

    def __init__(self, titulo, descripcion, prioridad, estado, administrador):
        self.__ids = 0
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__prioridad = prioridad
        self.__estado = estado
        self.__administrador = administrador

    def get_id(self):
        return self.__ids

    def get_titulo(self):
        return self.__titulo

    def get_descripcion(self):
        return self.__descripcion

    def get_prioridad(self):
        return self.__prioridad

    def get_estado(self):
        return self.__estado

    def get_administrador(self):
        return self.__administrador

    def set_id(self, ids):
        self.__ids = ids

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_prioridad(self, prioridad):
        self.__prioridad = prioridad

    def set_estado(self, estado):
        self.__estado = estado

    def save(self):
        sql = 'insert into tickets(titulo, descripcion, prioridad, estado, administrador_id) values(%s,%s,%s,%s,%s)'
        val = (self.get_titulo(), self.get_descripcion(), self.get_prioridad(), self.get_estado(), self.get_administrador().get_id())
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
