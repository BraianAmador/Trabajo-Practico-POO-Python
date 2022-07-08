from mySql import dba


class Producto():
    def __init__(self, descripcion, codigoMarca, modelo, precio, factura):
        self.__ids = 0
        self.__descripcion = descripcion
        self.__codigoMarca = codigoMarca
        self.__modelo = modelo
        self.__precio = precio
        self.__factura = factura

    def get_id(self):
        return self.__ids

    def get_descripcion(self):
        return self.__descripcion

    def get_codigoMarca(self):
        return self.__codigoMarca

    def get_modelo(self):
        return self.__modelo

    def get_precio(self):
        return self.__precio

    def get_factura(self):
        return self.__factura

    def set_id(self, ids):
        self.__ids = ids

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_codigoMarca(self, codigoMarca):
        self.__codigoMarca = codigoMarca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_precio(self, precio):
        self.__precio = precio

    def save(self):
        sql = 'insert into productos (descripcion, marca_id, modelo, precio, factura_id) values(%s, %s,%s,%s,%s)'
        val = (self.get_descripcion(), self.get_codigoMarca(), self.get_modelo(), self.get_precio(), self.get_factura().get_id())
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)