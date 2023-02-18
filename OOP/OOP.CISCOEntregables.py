import math
import sys 
import math, sys 

import math
print(math.sin(math.pi/2))

import math


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

from math import pi

print(math.e)

from math import sin, pi

print(sin(pi/2))



pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

#from module import * #El asterisco importa todas las entidades del modulo
#import module as alias #as es palabra reservada que asigna un alias al modulo

import math as m

print(m.sin(m.pi/2))

#También funciona para entidades del módulo, as asigna un alias

from math import pi as PI, sin as sine

print(sine(PI/2))

#Módulos útiles
for name in dir(math)
    print (name, end = "\t")

#Se puede ejecutar sin necesidad del script previamente el módulo está importado, 
# si no lo estuviera hay que importarlo
dir(math)

#Algunas funciones de math

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

#sin(x) --> Seno de x
#cos(x) --> Coseno de x
#tan(x) --> Tangente de x
#asin (x) --> Arcoseno de x
#acos (x) --> arcocoseno de x
#atan (x) --> arcotangente de x
#pi --> constante con valor de pi
#radians (x) --> convierte x de grados a radianes
#degrees (x) --> convierte x de radianes a grados
#sinh(x) → el seno hiperbólico.
#cosh(x) → el coseno hiperbólico.
#tanh(x) → la tangente hiperbólico.
#asinh(x) → el arcoseno hiperbólico.
#acosh(x) → el arcocoseno hiperbólico.
#atanh(x) → el arcotangente hiperbólico.

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

#e → una constante con un valor que es una aproximación del número de Euler (e).
#exp(x) → encontrar el valor de ex.
#log(x) → el logaritmo natural de x.
#log(x, b) → el logaritmo de x con base b.
#log10(x) → el logaritmo decimal de x (más preciso que log(x, 10)).
#log2(x) → el logaritmo binario de x (más preciso que log(x, 2)).
#pow(x, y) → encuentra el valor de xy (toma en cuenta los dominios).

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

#ceil(x) → devuelve el entero más pequeño mayor o igual que x.
#floor(x) → el entero más grande menor o igual que x.
#trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
#factorial(x) → devuelve x! (x tiene que ser un valor entero y no negativo).
'''hypot(x, y) → devuelve la longitud de la hipotenusa de un triángulo rectángulo con las 
longitudes de los catetos iguales a (x) y (y) (lo mismo que sqrt(pow(x, 2) + pow(y, 2)) pero más preciso).
'''
'''La función general llamada random() (no debe confundirse con el nombre del módulo) 
produce un número flotante x entre el rango (0.0, 1.0) - en otras palabras: (0.0 <= x < 1.0).'''

from random import random

for i in range(5):
    print(random())

'''La función seed() es capaz de directamente establecer la semilla 
del generador. Te mostramos dos de sus variantes'''

from random import random, seed

seed(0)

for i in range(5):
    print(random())



from random import randrange, randint

print(randrange(1), end=' ')   #(randrange(fin))
print(randrange(0, 1), end=' ')  #(randrange(inicio, fin)) inicio incluyente fin excluyente
print(randrange(0, 1, 1), end=' ')  #(randrange(inicio, fin, incremento))
print(randint(0, 1))                  #(randint(izquierda, derecha)) izq y der incluyentes

#ejercicio
from random import randint

#choice(secuencia)
#sample(secuencia, elementos_a_elegir=1)

for i in range(10):
    print(randint(1, 10), end=',')

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

'''El módulo platform permite acceder a los datos de la plataforma 
subyacente, es decir, hardware, sistema operativo e información sobre la versión del intérprete.'''

'''Así es como se puede invocar:'''
#platform(aliased = False, terse = False)
'''Y ahora:
aliased → cuando se establece a True (o cualquier valor distinto a cero) 
puede hacer que la función presente los nombres de capa subyacentes alternativos en lugar de los comunes.'''
'''terse → cuando se establece a True (o cualquier valor distinto a cero) 
puede convencer a la función de presentar una forma más breve del resultado (si lo fuera posible).
'''
from platform import platform

print(platform())
print(platform(1)) #hace que la función presente los nombres de capa subyacentes alternativos en lugar de los comunes
print(platform(0, 1)) #puede convencer a la función de presentar una forma más breve del resultado

'''En ocasiones, es posible que solo se desee conocer el nombre genérico del procesador 
que ejecuta el sistema operativo junto con Python y el código, 
una función llamada machine() te lo dirá. Como anteriormente, la función devuelve una cadena.'''
from platform import machine

print(machine())

'''La función processor() devuelve una cadena con el nombre real del procesador (si lo fuese posible).'''
from platform import processor

print(processor())

'''Una función llamada system() devuelve el nombre genérico del sistema operativo en una cadena.'''
from platform import system

print(system())


'''La versión del sistema operativo se proporciona como una cadena por la función version().'''
from platform import version

print(version())


'''python_implementation() → devuelve una cadena que denota la implementación de Python 
(espera CPython aquí, a menos que decidas utilizar cualquier rama de Python no canónica).
python_version_tuple() → devuelve una tupla de tres elementos la cual contiene:
    La parte mayor de la versión de Python.
    La parte menor.
    El número del nivel de parche.'''
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

'''Puedes leer sobre todos los módulos estándar de Python aquí: https://docs.python.org/3/py-modindex.html.'''

#Ejercicio 1
import math
result = math.e == math.exp(1)

#True

#Ejercicio 4
import platform

print(len(platform.python_version_tuple()))

#3







