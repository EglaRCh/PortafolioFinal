'''La herencia es un mecanismo de 
la programación orientada a objetos
que sirve para crear clases nuevas a partir
de clases preexistentes. Se toman (heredan)
atributos y comportamientos de las clases viejas
y se modifica para modelar una nueva situación'''

class Tarjeta:
    def __init__(self, numero, cuentah, caducidad, estado, banco, cantidad = 0):
        self.numero = numero
        self.cuentahabiente = cuentah
        self.caducidad = caducidad
        self.estado = estado
        self.saldo = cantidad
        self.banco = banco
        return
    def __str__(self):
        return 'Tarjeta número {} del cuentahabiente {} \n tiene una fecha de expiración {}, \nEstado de la cuenta {}, \nBanco {}, \nCuenta con un saldo ${}'.format(self.banco,self.numero,self.cuentahabiente,self.caducidad,self.estado,str(self.saldo))
    
    def deposito (self, cantidadx): #tiene una x porque es el parámetro, el cual puede ser cualquier valor ingresado
        if self.estado == 'Inactiva':
            msg = 'La tarjeta está Inactiva, por favor acudir a sucursal'
        else:
            self.saldo += cantidadx
            msg = 'El saldo nuevo de la tarjeta es {}'.format(self.saldo)
        return msg


    def retirar (self, cantidadx):
        if self.estado == 'Inactiva':
            msg = 'La tarjeta esta Inactiva, por favor acudir a sucursal'
        else:
            if self.saldo < cantidadx:
                msg = 'Saldo insuficiente para el retiro'
            else: 
                self.saldo -= cantidadx
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

class Debito (Tarjeta):
    def __init__(self, numero, cuentah, caducidad, estado,tipo, banco, emisor, cantidad = 0):
        self.tipo = tipo
        self.emisor = emisor
        super().__init__(numero, cuentah, caducidad, estado, banco, cantidad)
        return
    
    def __str__(self):
        return Tarjeta.__str__(self) + '\nTipo de Tarjeta {1} \nEmisor: {0}'.format(self.emisor, self.tipo)

    def usoDebito (self):
        print('Recuerda que solamente puedes ocupar tu saldo en la cuenta')

deb = Debito('9110001', 'Angélica Maria', '01/26','Inactiva','Débito','Banorte','Visa', 2500)

print (deb)
print(deb.banco) #banorte

deb.activar()
deb.anular()
deb.deposito(500)

print(deb.emisor)
print(deb.cuentahabiente)

deb.usoDebito()
deb.retirar(500)
deb.deposito(5000)

print(deb)

class Credito (Tarjeta):
    def __init__(self, numero, cuentah, caducidad, estado, tipo, banco, emisor, limite, cantidad = 0):
        self.tipo = tipo
        self.emisor = emisor
        self.limite = limite
        super().__init__(numero, cuentah, caducidad, estado, banco, cantidad)
        return
    
    def __str__(self):
        return Tarjeta.__str__(self) + '\nTipo de Tarjeta {} \nLimite de Crédito: ${}'. format(self.tipo, self.emisor, self.limite)

    def usoCredito (self):
        print ('Recuerda que debes pagar tu Crédito')

tdc = Credito('9110001', 'Angélica Maria', '01/26','Inactiva','Débito','Banorte','Visa', 3500, 2500)

print(tdc)

tdc.deposito(12000)
tdc.retirar (5000)
tdc.activar()
tdc.limite = 4500
print(tdc.caducidad)
print(tdc.limite)

class Puntos(Tarjeta):
    def __init__(self, numero, cuentah, caducidad, estado, banco, tipo, cantidad=0):
        self.tipo  = tipo
        super().__init__(numero, cuentah, caducidad, estado, banco, cantidad)
        return
    def __str__(self):
        return Tarjeta.__str__(self + '\nTipo de Tarjeta {}'.format(self.tipo))
    
    def usoPuntos (self):
        print ('Recuerda ver las promociones particulares')

puntos = Puntos('9110001', 'Angélica Maria', '01/26','Inactiva','Débito','Banorte','Puntos Premia', 500)

print(puntos)

puntos.activar()

td = Debito('9110001', 'Angélica Maria', '01/26','Inactiva','Débito','Banorte','Visa', 2500)
tdc = Credito ('9110001', 'Angélica Maria', '01/26','Inactiva','Débito','Banorte','Visa', 2500)


Objeto=[]
Objeto.append(Credito ('9110001', 'Angelica Maria', '05/26', 'Inactiva', 'Credito','HSBC','Mastercard',35000 ,2500))
Objeto.append(Credito ('9110002', 'Rosa Mendez', '05/26', 'Inactiva', 'Credito','HSBC','Mastercard',35000 ,2500))
Objeto.append(Credito ('9110003', 'Angel Moreno', '05/26', 'Inactiva', 'Credito','HSBC','Mastercard',35000 ,2500))
Objeto.append(Debito ('9120001', 'Angelica Maria', '05/26', 'Inactiva', 'Debito', 'Banorte', 'Visa',2500 ))
Objeto.append(Debito ('9120001', 'Rosa Maria', '05/26', 'Inactiva', 'Debito', 'Banorte', 'Visa',2500 ))
Objeto.append(Puntos ('9130001', 'Angelica Maria', '05/26', 'Inactiva', 'Banamex','Puntos Premia', 500))

x=1
for objetos  in Objeto:
    print("**********************")
    print("Numero de Tarjetahabientes [', x, '] ")
    print(objetos)
    print("**********************")
    x += 1



