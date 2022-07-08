import base64
from mySql import dba


class Administrador():
    def __init__(self, nombre, apellido, mail, interno, password):
        self.__ids = 0
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__interno = interno
        self.set_password(password)

    def get_id(self):
        return self.__ids

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_mail(self):
        return self.__mail

    def get_interno(self):
        return self.__interno

    def get_password(self):
        return self.__password

    def set_id(self, ids):
        self.__ids = ids

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_mail(self, mail):
        self.__mail = mail

    def set_interno(self, interno):
        self.__interno = interno

    def set_password(self, password):
        self.__password = self.encriptarPass(password)

    def encriptarPass(self, password):
        return base64.encodebytes(bytes(password, 'utf-8')).decode('utf-8')

    def desencriptarPass(self, password):
        return base64.decodebytes(password.encore("UTF-8")).decode('utf-8')

    def save(self):
        sql = 'insert into administrador(nombre, apellido, mail, interno, password) values(%s,%s,%s,%s,%s)'
        val = (self.get_nombre(), self.get_apellido(), self.get_mail(), self.get_interno(), self.get_password())
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self):
        sql = 'delete from administrador where administrador_id=%s'
        val = (self.get_id(),)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def update_nombre(self, nombre):
        sql = 'update administrador set nombre=%s where administrador_id=%s '
        val = (nombre, self.__ids)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def update_apellido(self, apellido):
        sql = 'update administrador set apellido=%s where administrador_id=%s '
        val = (apellido, self.__ids)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def update_mail(self, mail):
        sql = 'update administrador set mail=%s where administrador_id=%s '
        val = (mail, self.__ids)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def update_interno(self, interno):
        sql = 'update administrador set interno=%s where administrador_id=%s '
        val = (interno, self.__ids)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()

    def update_password(self, password):
        sql = 'update administrador set password=%s where administrador_id=%s '
        val = (password, self.__ids)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()




