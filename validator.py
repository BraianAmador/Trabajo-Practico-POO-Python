import base64
from validate_email import validate_email
from mySql import dba


class Validator():

    def __init__(self):
        pass

    def validar_usuario(self, dicc):
        datosFinales = {}
        errores = {}

        for x, y in dicc.items():
            datosFinales[x] = y.strip()
        if datosFinales['nombre'] == '':
            errores['nombre'] = 'Campo nombre vacio'
        if datosFinales['apellido'] == '':
            errores['apellido'] = 'Campo apellido vacio'
        if datosFinales['telefono'] == '':
            errores['telefono'] = 'Campo telefono vacio'
        if datosFinales['codigoSector'] == '':
            errores['codigoSector'] = 'Campo numero vacio'
        elif not datosFinales['codigoSector'].isdigit():
            errores['codigoSector'] = 'El numero contiene un caracter'

        if errores == {}:
            sql = 'select usuario_id from usuarios where telefono=%s'
            val = (datosFinales['telefono'],)
            dba.get_cursor().execute(sql, val)
            result = dba.get_cursor().fetchone()
            if result is not None:
                errores['telefono'] = 'El numero existe en el sistema'
                return errores
        return errores

    def validar_sector(self, dicc):
        datosFinales = {}
        errores = {}

        for x, y in dicc.items():
            datosFinales[x] = y.strip()
        if datosFinales['nombre'] == '':
            errores['nombre'] = 'Campo nombre vacio'

        if errores == {}:
            sql = 'select sector_id from sectores where nombre=%s'
            val = (datosFinales['nombre'],)
            dba.get_cursor().execute(sql, val)
            result = dba.get_cursor().fetchone()
            if result is not None:
                errores['nombre'] = 'El sector existe en el sistema'
                return errores
        return errores

    def validar_marca(self, dicc):
        datosFinales = {}
        errores = {}

        for x, y in dicc.items():
            datosFinales[x] = y.strip()
        if datosFinales['nombre'] == '':
            errores['nombre'] = 'Campo nombre vacio'

        if errores == {}:
            sql = 'select marca_id from marcas where nombre=%s'
            val = (datosFinales['nombre'],)
            dba.get_cursor().execute(sql, val)
            result = dba.get_cursor().fetchone()
            if result is not None:
                errores['nombre'] = 'La marca ya existe en el sistema'
                return errores
        return errores

    def validar_factura(self, dicc):
        datosFinales = {}
        errores = {}

        for x, y in dicc.items():
            datosFinales[x] = y.strip()
        if datosFinales['numero'] == '':
            errores['numero'] = 'Campo numero vacio'
        if datosFinales['fechaDeCompra'] == '':
            errores['fechaDeCompra'] = 'Campo fecha vacio'
        if datosFinales['codigoProveedor'] == '':
            errores['codigoProveedor'] = 'Campo proveedor vacio'
        elif not datosFinales['codigoProveedor'].isdigit():
            errores['codigoProveedor'] = 'El campo proveedor contiene un caracter'

        if errores == {}:
            sql = 'select factura_id from facturas where numero=%s'
            val = (datosFinales['numero'],)
            dba.get_cursor().execute(sql, val)
            result = dba.get_cursor().fetchone()
            if result is not None:
                errores['numero'] = 'El numero existe en el sistema'
                return errores
        return errores

    def validar_proveedor(self, dicc):
        datosFinales = {}
        errores = {}

        for x, y in dicc.items():
            datosFinales[x] = y.strip()
        if datosFinales['nombre'] == '':
            errores['nombre'] = 'Campo nombre vacio'
        if datosFinales['direccion'] == '':
            errores['direccion'] = 'Campo direccion vacio'
        if datosFinales['telefono'] == '':
            errores['telefono'] = 'Campo telefono vacio'
        if datosFinales['localidad'] == '':
            errores['localidad'] = 'Campo numero vacio'

        if errores == {}:
            sql = 'select proveedor_id from proveedores where telefono=%s'
            val = (datosFinales['telefono'],)
            dba.get_cursor().execute(sql, val)
            result = dba.get_cursor().fetchone()
            if result is not None:
                errores['telefono'] = 'El numero de telefono existe en el sistema'
                return errores
        return errores

    def validar_administrador(self, dicc):
        datosFinales = {}
        errores = {}
        caracteresEspeciales = ['$', '@', '#', '%']

        for x, y in dicc.items():
            datosFinales[x] = y.strip()

        if datosFinales['nombre'] == '':
            errores['nombre'] = 'Campo nombre vacio'
        if datosFinales['apellido'] == '':
            errores['apellido'] = 'Campo apellido vacio'
        if datosFinales['mail'] == '':
            errores['mail'] = 'Campo mail vacio'
        if not validate_email(datosFinales['mail']):
            errores['mail'] = 'No tiene formato de mail'
        if datosFinales['interno'] == '':
            errores['interno'] = 'Campo telefono vacio'
        if datosFinales['password'] == '':
            errores['password'] = 'Campo password vacio'
        elif len(datosFinales['password']) < 6:
            errores['password'] = 'La password debe tener al menos 6 caracteres'
        elif not any(i.isupper() for i in datosFinales['password']):
            errores['password'] = 'La password debe tener al menos 1 caracter con mayuscula'
        elif not any(i.islower() for i in datosFinales['password']):
            errores['password'] = 'La password debe tener al menos 1 caracter con minuscula'
        elif not any(i in caracteresEspeciales for i in datosFinales['password']):
            errores['password'] = 'La password debe tener al menos 1 caracter con especial'
        elif datosFinales['password'] != datosFinales['cpassword']:
            errores['password'] = 'la password no coincide'

        if errores == {}:
            sql = 'select administrador_id from administrador where mail=%s'
            val = (datosFinales['mail'],)
            dba.get_cursor().execute(sql, val)
            result = dba.get_cursor().fetchone()
            if result is not None:
                errores['mail'] = 'Ya se registro este mail intente con otro!'
                return errores

        return errores

    def validar_login(self, dicc):

        datosFinales = {}
        errores = {}

        for x, y in dicc.items():
            datosFinales[x] = y.strip()

        sql = "select password from administrador where mail=%s"
        val = (datosFinales['mail'],)
        dba.get_cursor().execute(sql, val)

        result = dba.get_cursor().fetchone()

        if result is None:
            errores['mail'] = "el mail ingresado no existe en la base"
            return errores

        if base64.decodebytes(result[0].encode("UTF-8")).decode('utf-8') == datosFinales['password']:
            #return base64.decodebytes(result[0].encode("UTF-8")).decode('utf-8')
            return None
        else:
            errores['password'] = "la password es incorrecta"
            return errores

    def validar_asignacion(self, dicc):
        datosFinales = {}
        errores = {}

        for x, y in dicc.items():
            datosFinales[x] = y.strip()
        if datosFinales['codigoProducto'] == '':
            errores['codigoProducto'] = 'Campo nombre vacio'
        if not datosFinales['codigoProducto'].isdigit():
            errores['codigoProducto'] = 'El numero contiene un caracter'
        if datosFinales['codigoUsuario'] == '':
            errores['codigoUsuario'] = 'Campo numero vacio'
        elif not datosFinales['codigoUsuario'].isdigit():
            errores['codigoUsuario'] = 'El numero contiene un caracter'

        return errores

    def validar_ticket(self, dicc):
        datosFinales = {}
        errores = {}

        for x, y in dicc.items():
            datosFinales[x] = y.strip()
        if datosFinales['titulo'] == '':
            errores['titulo'] = 'Campo titulo vacio'
        if datosFinales['descripcion'] == '':
            pass
        if datosFinales['prioridad'] == '':
            errores['prioridad'] = 'Campo prioridad vacio'
        elif not datosFinales['prioridad'].isdigit():
            errores['prioridad'] = 'Prioridad contiene un caracter'
        if datosFinales['estado'] == '':
            errores['estado'] = 'Campo estado vacio'
        elif not datosFinales['estado'].isdigit():
            errores['estado'] = 'Estado contiene un caracter'
        return errores

    def validar_producto(self, dicc):
        datosFinales = {}
        errores = {}

        for x, y in dicc.items():
            datosFinales[x] = y.strip()
        if datosFinales['descripcion'] == '':
            errores['descripcion'] = 'Campo descripcion vacio'
        if datosFinales['codigoMarca'] == '':
            errores['codigoMarca'] = 'Campo marca vacio'
        if datosFinales['modelo'] == '':
            errores['modelo'] = 'Campo modelo vacio'
        if datosFinales['precio'] == '':
            errores['precio'] = 'Campo precio vacio'
        elif not datosFinales['precio'].isdigit():
            errores['precio'] = 'El precio contiene un caracter'

        return errores

val = Validator()
