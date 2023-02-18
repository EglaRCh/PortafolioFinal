'''Errores'''
#el usuario siempre podrá ingresar cadena de caracteres
#completamente arbitraria (Esto puede ser una vulnerabilidad)
#Hay que protegerse de tales sorpresas
import math

x= float(input('Ingresa x:'))
y= math.sqrt(x)

print('La raíz cuadrada de', x, 'es gual a', y)

#ZeroDivisionError #No se puede dividir entre cero
'''value = 1
value /= 0'''

#IndexError #No existe el índice buscado
'''my_list = []
x=my_list[0]'''

#Revisión de código funcional en esta única aplicación NO ES TRY
first_number = int(input('ingresa el primer numero: '))
second_number = int(input('ingresa el segundo numero: '))

if second_number != 0 :
    print(first_number/second_number)
else:
    print('esta operacion no puede ser realizada')

print('Fin')

#Enfoque favorito de Python TRY
first_numberr = int (input('Ingresa el primer numero'))
second_numberr = int(input('Ingresa el segundo numero'))

try:
    print(first_numberr/second_numberr)
except:
    print('Esta operación no puede ser realizada')

print('Fin')

'''En el primer paso, Python intenta realizar todas las 
instrucciones colocadas entre las instrucciones try: y except:.
Si no hay ningún problema con la ejecución y todas las 
instrucciones se realizan con éxito, la ejecución salta al 
punto después de la última línea del bloque except: , y la 
ejecución del bloque se considera completa.
Si algo sale mal dentro del bloque try: o except:, la ejecución 
salta inmediatamente fuera del bloque y entra en la primera instrucción 
ubicada después de la palabra clave reservada except:, esto significa 
que algunas de las instrucciones del bloque pueden ser silenciosamente 
omitidas.'''

#Otro experimento con try: y except general
try:
    print("1")
    x = 1/0
    print("2") #este dos no se imprimirá porque el ZeroDivisionError se encuentra previamente a su código, entonces ahí se detiene el programa
except: 
    print('Oh cielos, algo salió mal...')

print ('3')

#Cuando sólo se buscan las excepciones en general no se obiene mucha información acerca de la razón del error
#EJEMPLO
try: 
    x= int(input('ingresa un número: '))
    y=1/x
except:
    print('Oh cielos, algo salió mal')
print('FIN')
    
#en el ejemplo anterior puede pasar que 
#1) el usuario no ingresó enteros
#2)valor entero igual a 0 fue asignado a x
#pero el excep que se usa solo indica que hay un error ¿Cual? no se sabe
#Para resolver esto se utiliza la siguiente forma: 
'''try:
    :
except exc1:
    :
except exc2:
    : '''

'''Si el try genera la excepción exc1, esta será manejada por el bloque except exc1:.
De la misma manera, si el try genera la excepción exc2, esta será manejada por el bloque except exc2:.
Si el try genera cualquier otra excepción, será manejado por el bloque sin nombre except.'''

try:
    x=int(input('Ingresa un número: '))
    y=1/0
    print(y)
except ZeroDivisionError:
    print('No puedes dividir entre cero, lo siento')
except ValueError:
    print('Debes ingresar un valor entero')
except: #Except genérico
    print('Oh cielos, algo salió mal')

print('Fin')

#NOTA: recuerda! Crtl-C es una interrupción del usuario! 
#lo anterior provoca un KeyboardInterrupt

#OTRO experimento
#en el siguiente código, al no encontrarse el bloque except ZeroDivisionError ni el bloque except genérico, el programa arroja en la consola el nombre de la excepción tal cual se conoce en Python, sin niguna instrucción

'''try:
    x=int(input('Ingresa un número: '))
    y=1/0
    print(y)
except ValueError:
    print('Debes ingresar un valor entero')'''

#Otros códigos
try:
    print("Tratemos de hacer esto")
    print("#"[2]) #IndexError no específicado en un bloque except
    print("¡Tuvimos éxito!")
except:
    print("Hemos fallado")
print("Hemos terminado")

try:
    print('alpha'[1/0])
except ZeroDivisionError:
    print('cero') #la unica linea de código y primera, encontramos una lista con una división entre cero
except IndexingError:#???
    print('indice')
except:
    print('algo')

#Ejemplo de la jerarquí de excepciones
try:
    y=1/0
except ArithmeticError:  
    print('Uuuuuppsss...')
print('Fin')

#ZeroDivisionError se encuentra en ArithmeticError, este a su vez se encuentra dentro de Exception a su vez dentro de BaseException
#Se puede colocar cualquiera de esas excepeciones y seguirá el mensaje especificado 'Uuupppss...'

#¿Qué pasa si coloco una excepción más general que la siguiente?
try:
    y=1/0
except ArithmeticError:
    print('problema aritmetico')
except ZeroDivisionError:
    print('Division entre cero')
print('Fin')

#Entonces, el código enviará el mensaje del primer bloque except que encuentre en el código

#Si una execpci+on es generada dentro de una función puede ser manejada
#DENTRO de la función
#FUERA de la función

#DENTRO de la funcion
def bad_fun(n):
    try:
        return 1/n
    except ArithmeticError:
        print('Problema aritmético')
    return None

bad_fun(0) #Problema aritmético

#FUERA de la función
def bad_funn(n):
    return 1/n

try:
    bad_funn(0)
except ArithmeticError:
    print('Qué pasó? ¡Se generó una excepción!')

'''NOTA:la excepción generada puede cruzar la función y los límites del módulo, 
y viajar a través de la cadena de invocación buscando una cláusula except capaz 
de manejarla.
Si no existe tal cláusula, la excepción no se controla y Python resuelve el 
problema de la manera estándar - terminando el código y emitiendo un mensaje de diagnóstico.'''

#¿Cómo probar la rutina de manejo de excepciones sin forzar al código a hacer cosas incorrectas?
#raise

def bad_fun(n):
    raise ZeroDivisionError

try: 
    bad_fun(0)
except ArithmeticError:
    print ('¿Qué pasó? ¿Un error?')

print('Fin')

#raise cuando toma en cuenta la ausencia del nombre de la excepcion
#existe una SERIA RESTRICCIÓN: esta variante de la instrucción raise
#solo puede ser UTILIZADA dentro del bloque except; en cualquier otro 
#contexto causa error
def bad_funs(n):
    try:
        return n/0
    except:
        print('Lo hice otra vez!')
        raise

try: 
    bad_funs(0)
except ArithmeticError:
    print('Ya veo!')

print('Fin')

'''La excepción ZeroDivisionError es generada dos veces
-Primero, dentro del try debido a que se intentó realizar una división entre cero
-Segundo, dentro de la parte except por la instruccion raise'''

# assert   (afirmar) ---> assert expression
#si la afirmación es falsa genera una excepción AssertionError, asegurándose de que tu código no produzca resultados no válidos y muestra claramente la naturaleza de la falla
#Las aserciones no reemplazan las excepciones NI validan los datos, son suplementos
#ejemplo
import math

x=float(input('Ingresa un número: '))
assert x >= 0.0

x = math.sqrt(x)
print(x)

def foo(x):   #por qué este código devuelve 'algo'?!?!?1
    assert x
    return 1/x

try:
    print(foo(0))
except ZeroDivisionError:
    print("cero")
except:
    print("algo")

#KeyboradInterrrupt: esta excepción no se deriva de la clase Exception. Ejecuta el programa IDLE

'''from time import sleep
seconds=0
while True:
    try:
        print(seconds)
        seconds +=1
        sleep(1)
    except KeyboardInterrupt:
        print('No hagas eso')''' #NO PUEDE SER TERMINADO PRESIONANDO Ctrl-C

#MemoryError: se genera una excepción concreta cuando no se puede conplatar una operación debido a la falta de memoria libre
#OverflowError: surge cuando una operación produce un número demasiado grande para ser almacenado con éxito

from math import exp
ex=1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
        print('El numero es demasiado grande')

#ImportError: se genera una excepción concreta cuando falla una operación de importación.
try:
    import math
    import time
    import abracadabra

except: 
    print('Una de tus importaciones ha fallado.')











