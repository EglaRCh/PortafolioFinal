class Tarjeta:
    #__init__ <-- initialization #Siempre que comiencen con __ "doble guión bajo", son propiedades de Python itself
    def __init__(self, numero, cuenta, caducidad, estado, banco, cantidad = 0): #self--> lo que tenga a continución es MI ATRIBUTO
        self.numero = numero
        self.cuentahabiente = cuenta
        self.caducidad = caducidad
        self.estado = estado
        self.banco = banco
        self.saldo = cantidad
        return

    def __str__(self): #str ayuda a obtener una impresión
        return 'Banco: {}, \nTarjeta número: {}, del cuenta habiente: {}, \nTiene una fecha de expiración: {}, \nEstado de la cuenta: {}, \nCuenta con un saldo:  ${}'.format(self.banco,self.numero,self.cuentahabiente,self.caducidad,self.estado,str(self.saldo))
      
    def deposito (self, cantidadx): #tiene una x porque es el parámetro, el cual puede ser cualquier valor ingresado
        self.saldo += cantidadx
        return 'El saldo nuevo dela tarjeta es {}'.format(self.saldo)

    def retirar (self, cantidadx):
        if self.saldo < cantidadx:
            msg = 'El saldo es insuficiente para el retiro'.format(self.saldo)
        else:
            self.saldo >= cantidadx
            msg = 'El saldo nuevo de la tarjeta es {}'.format(self.saldo)
        print (msg)
    
    def mostrar_saldo (self):
        print('El saldo actual de la cuenta es $: ', self.saldo)

    def activar (self):
        self.estado = 'Activa'
        return 
    
    def anular (self):
        self.estado = 'Inactiva'
        return

    def mostrar_estatus(self):
        print('El estado de la tarjeta actual es: ', self.estado)
    
    def asignacionbanco (self,bancos):
        self.banco = bancos
        print('Proceso de actualización de Banco satisfactoria')
        return

    def __str__(self):
    return 'Tarjeta número {} del derechohabiente {} \n tiene una fecha de expiración {}, \nEstado de la cuenta {}, \nBanco {}, \nCuenta con un saldo de ${}'


class Debito(Tarjeta):
    def__init__(self, numero, cuentah, estado, tipo, banco, emisor, cantidad = 0 ):
        self.tipo = tipo
        self.emisor = emisor
        super().__init__(numero, cuentah, caducidad, estado, banco, cantidad)
        return
    

    #Creacion de instancias
t = Tarjeta('9110010', 'Juan Lopez', '05/23', 'Inactiva', 'Banamex', 3)
t2 = Tarjeta('9110011', 'Monica Naranjo', '05/23', 'Inactiva', 'HSBC', 0)
t3= Tarjeta('9110012', 'Pedtro Garcia', '05/23', 'Inactiva', 'Bancomer', 3000)
t4= Tarjeta('9875623', 'Juan Lopez', '05/24', 'Inactiva', 'Banorte', 1000)
t5= Tarjeta('9875624', 'Juan Lopez', '05/24', 'Inactiva', '', 1000)
t6= Tarjeta('9875625', 'Juan Lopez', '05/24', 'Inactiva', 'Banorte')
t7= Tarjeta('9875626', 'Sofia MOrales', '', 'Inactiva', 'Banorte')