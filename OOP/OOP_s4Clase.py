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

#Creacion de instancias
t = Tarjeta('9110010', 'Juan Lopez', '05/23', 'Inactiva', 'Banamex', 3)
t2 = Tarjeta('9110011', 'Monica Naranjo', '05/23', 'Inactiva', 'HSBC', 0)
t3= Tarjeta('9110012', 'Pedtro Garcia', '05/23', 'Inactiva', 'Bancomer', 3000)
t4= Tarjeta('9875623', 'Juan Lopez', '05/24', 'Inactiva', 'Banorte', 1000)
t5= Tarjeta('9875624', 'Juan Lopez', '05/24', 'Inactiva', '', 1000)
t6= Tarjeta('9875625', 'Juan Lopez', '05/24', 'Inactiva', 'Banorte')
t7= Tarjeta('9875626', 'Sofia MOrales', '', 'Inactiva', 'Banorte')

#Impresion de la inicialización del objeto
print(t)
print('************************************')
print(t2)
print('************************************')
print(t3)
print('************************************')
print(t4)
print('************************************')
print(t5)
print('************************************')
print(t6)
print('************************************')
print(t7)

#Uso de métodos en el objeto
#objeto.método
t.activar()
t2.activar()
t3.activar() #cambia el parámetro del atribudo del objeto tarjeta 3

t3.anular() #lo vuelve a cambiar

t.mostrar_saldo()
t2.mostrar_saldo()
t3.mostrar_saldo()
t4.mostrar_saldo()
t5.mostrar_saldo()
t6.mostrar_saldo()
t7.mostrar_saldo()

t.deposito(200)

t2.deposito

t3.deposito(600)

t3.deposito(300)

t.retirar(800)

t.retirar(80)

t.mostrar_saldo()

t2.mostrar_saldo()

t4.mostrar_estatus()

print(t4)

print('Bienvenido al menú interactivo')

while(True):
    print("""¿Qué quieres hacer? Escribe una opción:
    1)Agregar monto
    2)Retirar monto
    3)Mostrar saldo
    4)Activar tarjeta
    5)Inactivar tarjeta
    6)Mostrar estatus de tarjeta
    7)Salir""")
    opcion = input()
    if opcion == '1':
        monto = float(input('Indica el monto a agregar:'))
        t4.deposito(monto)
    elif opcion == '2':
        monto = float(input('Indica el monto a retirar:'))
        t4.retirar(monto)
    elif opcion == '3':
        t4.mostrar_saldo()
    elif opcion == '4':
        t4.activar()
        print(t4)
    elif opcion == '5':
        t4.anular()
        print(t4)
    elif opcion == '6':
        t4.mostrar_estatus()
    elif opcion == '7':
        print('Hasta luego! Un placer ayudarle')
        break
    else:
        print('Comando desconocido, por favor vuelva intentarlo')


#Lista de Objetos, se crea una lista vacía
listaOb =[]

#A esta lista se le van a agregar todos los objetos instanciados (tarjetas) #Se crea un arreglo

listaOb.append (Tarjeta('9110010', 'Juan Lopez', '05/23', 'Inactiva', 'Banamex', 3)) #0
listaOb.append (Tarjeta('9110011', 'Monica Naranjo', '05/23', 'Inactiva', 'HSBC', 0)) #1
listaOb.append (Tarjeta('9110012', 'Pedtro Garcia', '05/23', 'Inactiva', 'Bancomer', 3000)) #2
listaOb.append (Tarjeta('9875623', 'Juan Lopez', '05/24', 'Inactiva', 'Banorte', 1000)) #3
listaOb.append (Tarjeta('9875624', 'Juan Lopez', '05/24', 'Inactiva', '', 1000)) #4
listaOb.append (Tarjeta('9875625', 'Juan Lopez', '05/24', 'Inactiva', 'Banorte')) #5
listaOb.append (Tarjeta('9875626', 'Sofia MOrales', '', 'Inactiva', 'Banorte')) #6
    
#Ciclo para recorrer el arreglo previamente creado
x=0
for objetos in listaOb:
    print('********************')  
    print('Numero de índice  [', x, ']')
    print(objetos)
    print('********************')
    x+=1

buscar = input('Ingresa el número de tarjetahabienta para realizar tu búsqueda: ')
for objetos in listaOb:
    if objetos.numero == buscar:
        print('**************************')
        print(objetos)
        print('*****************++++++***')

listaOb[5].activar() #Aplicar un método a un índice específico del arreglo

from math import tan, radians
angle = int(input('Ingresa el angulo entero en grados: '))

#Debemos estar seguros de que angle != 90 + k *180
assert angle % 180 != 90
print(tan(radians(angle)))

#IndexError
#el código muestra una forma extravagante de dejar el bucle

the_list = [1,2,3,4,5]
ix =0
do_it=True

while do_it:
    try:
        print(the_list[ix])
        ix+= 1
    except IndexError:
        do_it=False

print('Listo')













