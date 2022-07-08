from mySql import dba


class Factura():
    def __init__(self, numero, fechaDeCompra, codigoProveedor):
        self.__ids = 0
        self.__numero = numero
        self.__fechaDeCompra = fechaDeCompra
        self.__codigoProveedor = codigoProveedor

    def get_id(self):
        return self.__ids

    def get_numero(self):
        return self.__numero

    def get_fechaDeCompra(self):
        return self.__fechaDeCompra

    def get_codigoProveedor(self):
        return self.__codigoProveedor

    def set_id(self, ids):
        self.__ids = ids

    def set_numero(self, numero):
        self.__numero = numero

    def set_fechaDeCompra(self, fechaDeCompra):
        self.__fechaDeCompra = fechaDeCompra

    def set_codigoProveedor(self, codigoProveedor):
        self.__codigoProveedor = codigoProveedor

    def save(self):
        sql = 'insert into facturas (numero, fechaDeCompra, proveedor_id) values(%s,%s,%s)'
        val = (self.get_numero(), self.get_fechaDeCompra(), self.get_codigoProveedor())
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
