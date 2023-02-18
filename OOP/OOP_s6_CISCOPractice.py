#generador - iteradir
for i in range(5):
    print(i)

#Protocolo iterador
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter


object = Class(8)

for i in Fib(10):
    print(i)

#yield -->  proporciona el valor de la expresión especificada 
# después de la palabra clave reservada yield, al igual que return, 
# pero no pierde el estado de la función.
#dicha función no debe invocarse explícitamente 
# ya que no es una función; es un objeto generador.

def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)

#-------

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)

'''Resultado
1
2
4
8
16
32
64
128'''

#La función list() puede transformar una serie de 
#invocaciones de generador en una lsita real

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = list(powers_of_2(3))
print(t)

#EL operador in  también te permite usar un generador.

def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n #pp = p ; p = n Esto sognifica lo anterior
            yield n

fibs = list(fibonacci(10))
print(fibs)

#listas por comprension TEORIA DE CONJUNTOS
list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]
 
print(list_1) #[1, 10, 100, 1000, 10000, 100000]
print(list_2) #[1, 10, 100, 1000, 10000, 100000]

#expresión condicional: forma de seleccionar 
#uno de dos valores diferentes en función del
#resultado de una expresión Booleana
the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)
'''Pero no es una instrucción condicional, 
No es una instrucción en absoluto es un operador'''

#Solo un cambio puede ocmpvertir cualquier compresion en un generador
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

'''¿Cómo puedes saber que la segunda asignación crea un generador, no una lista?
len(the_list) dará como resultado 10. Claro y predecible. len(the_generator) 
generará una excepción, y verás el siguiente mensaje:
Nota: la misma apariencia de la salida no significa que ambos bucles funcionen 
de la misma manera. 
En el primer bucle, la lista se crea (y se itera) como un todo; 
en realidad, existe cuando se ejecuta el bucle.
En el segundo bucle, no hay ninguna lista, solo hay valores 
subsecuentes producidos por el generador, uno por uno.'''

#La función lambda
# Los programadores usan la función lambda para simplificar el código, hacerlo más claro y fácil de entender
'''Afortunadamente, no es un problema, ya que se puede mandar llamar dicha función si realmente se necesita, pero, en muchos casos la función lambda puede existir y funcionar mientras permanece completamente de incógnito.'''

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

'''La parte más interesante de usar lambdas 
aparece cuando puedes usarlas en su forma pura: 
como partes anónimas de código destinadas a evaluar 
un resultado.'''
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

#map() aplica la función pasada por su primer argumento a todos los elementos 
# de su segundo argumento y devuelve un iterador que entrega todos los resultados de funciones subsequentes.

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

#lambdas y la función filter()
#filtra su segundo argumento mientras es guiado por direcciones que fluyen desde la función especificada 
# en el primer argumento (la función se invoca para cada elemento de la lista, al igual que en}
#filtra su segundo argumento mientras es guiado por direcciones que fluyen desde la función especificada en 
# el primer argumento (la función se invoca para cada elemento de la lista, al igual que en

from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

#cierres 
#Es cuna técnica que permite almacenar valores a pesar de que 
#el contexto en que se crearon ya no existe

'''Una función dentro de otra función solo se puede invocar
desde adentro de tal función, es una herrmaienta privada de la función
la función interna solo existe cuando se manda a llamar la externa'''

def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

#la funcion devuelta durante la invocación outer() es un cierre

#un cierre se debe invocar exactamente de la misma manera en que se ha declarado
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

#resultado
'''
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64'''

print(4|1)

#Abriendo el stream

try:
    stream = open("C:\Users\User\Desktop\file.txt", "rt")
    # El procesamiento va aquí.
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)

#diagnosticando problemas con los streams
try:
    # Algunas operaciones con streams.
except IOError as exc:
    print(exc.errno)

from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # El procesamiento va aquí.
    s.close()
except Exception as exc:
    print("El archivo no pudo ser abierto:", strerror(exc.errno))

# Se abre el archivo tzop.txt en modo lectura, devolviéndolo como un objeto del tipo archivo:
stream = open("tzop.txt", "rt", encoding = "utf-8")

# Se imprime el contenido del archivo:
print(stream.read())

from os import strerror

try:
    counter = 0
    stream = open('text.txt', "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

from os import strerror

try:
    counter = 0
    stream = open('text.txt', "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerr(e.errno))

from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('text.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('text.txt', 'rt')
    lines = stream.readlines(20)
    while len(lines) != 0:
        for line in lines:
            line_counter += 1
            for char in line:
                print(char, end='')
                character_counter += 1
        lines = stream.readlines(10)
    stream.close()
    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

from os import strerror

try:
	character_counter = line_counter = 0
	for line in open('text.txt', 'rt'):
		line_counter += 1
		for char in line:
			print(char, end='')
			character_counter += 1
	print("\n\nCaracteres en el archivo: ", character_counter)
	print("Líneas en el archivo:     ", line_counter)
except IOError as e:
	print("Se produjo un error de E/S:", strerror(e.errno))

from os import strerror

try:
	file = open('newtext.txt', 'wt') # Un nuevo archivo (newtext.txt) es creado.
	for i in range(10):
		s = "línea #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("Se produjo un error de E/S:", strerror(e.errno))

from os import strerror

try:
    file = open('newtext.txt', 'wt')
    for i in range(10):
        file.write("línea #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

from os import strerror

data = bytearray(10)

try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

from os import strerror

try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read())
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read(5))
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

from os import strerror

source_file_name = input("Ingresa el nombre del archivo fuente: ")
try:
    source_file = open(source_file_name, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)	

destination_file_name = input("Ingresa el nombre del archivo destino: ")
try:
    destination_file = open(destination_file_name, 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino:", strerror(e.errno))
    source_file.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = source_file.readinto(buffer)
    while readin > 0:
        written = destination_file.write(buffer[:readin])
        total += written
        readin = source_file.readinto(buffer)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) escritos con éxito')
source_file.close()
destination_file.close()

#Modulo os

import os

os.mkdir("my_first_directory")
print(os.listdir())

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())
os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())
os.mkdir("my_first_directory")
print(os.listdir())
os.rmdir("my_first_directory")
print(os.listdir())
returned_value = os.system("mkdir my_first_directory")
print(returned_value)

#modulo datetime
from datetime import date

today = date.today()

print("Hoy:", today)
print("Año:", today.year)
print("Mes:", today.month)
print("Día:", today.day)

from datetime import date
import time

timestamp = time.time()
print("Marca de tiempo:", timestamp)

d = date.fromtimestamp(timestamp)
print("Fecha:", d)
 
from datetime import date

d = date.fromisoformat('2019-11-04')
print(d)

#replace
from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

#weekday y isoweekday
from datetime import date

d = date(2019, 11, 4)
print(d.weekday()) #0

from datetime import date

d = date(2019, 11, 4)
print(d.isoweekday()) #1

#time(hour, minute, second, microsecond, tzinfo, fold)
from datetime import time

t = time(14, 53, 20, 1)

print("Tiempo:", t)
print("Hora:", t.hour)
print("Minuto:", t.minute)
print("Segundo:", t.second)
print("Microsegundo:", t.microsecond)

#módulo time
import time

class Student:
    def take_nap(self, seconds):
        print("Estoy muy cansado. Tengo que echarme una siesta. Hasta luego.")
        time.sleep(seconds)
        print("¡Dormí bien! ¡Me siento genial!")

student = Student()
student.take_nap(5)

#La función ctime() e convierte el tiempo en segundos desde el 1 de enero de 1970 (época Unix) en una cadena.

import time

timestamp = 1572879180
print(time.ctime(timestamp))

#las funciones gmtime() y localtime()
import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))
'''El ejemplo muestra dos funciones que convierten el tiempo transcurrido 
 desde la época Unix al objeto struct_time. La diferencia entre ellos es que
  la función gmtime devuelve el objeto struct_time en UTC, mientras que la 
  función localtime devuelve la hora local. Para la función gmtime, el 
  atributo tm_isdst es siempre 0.'''

#Las funciones asctime() y mktime() 
import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st)) #asctime -> convierte un objeto struct_time o una tupla en una cadena
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))#convierte un objeto struct_time o una tupla que expresa una hora local al número de segundos desde la época de Unix

'''
2019 => tm_year
11 => tm_mon
4 => tm_mday
14 => tm_hour
53 => tm_min
0 => tm_sec
0 => tm_wday
308 => tm_yday
0 => tm_isdst'''

#creación de objetos datetime
from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53)

print("Fecha y Hora:", dt)
print("Fecha:", dt.date()) #objeto con año mes día
print("Hora:", dt.time())  #objeto con la hora y minuto dados

#Métodos que devuelven la fecha y hora actuales
#today()  devuelve la fecha y hora local actual con el atributo 
# tzinfo establecido a None.
#now() devuelve la fecha y hora local actual igual que el método 
# today, a menos que le pasemos el argumento opcional tz. 
# El argumento de este método debe ser un objeto de la subclase tzinfo.

#utcnow() devuelve la fecha y hora UTC actual con el atributo tzinfo establecido a None

from datetime import datetime

print("hoy:", datetime.today())
print("ahora:", datetime.now())
print("utc_ahora:", datetime.utcnow())

#obtener una marca de tiempo
#El método timestamp devuelve un valor flotante que expresa el número de segundos 
# transcurridos entre la fecha y la hora indicadas por el objeto datetime y el 1 de enero de 1970, 00:00:00 (UTC).
from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Marca de tiempo:", dt.timestamp())

#método strftime 
'''El método strftime toma solo un argumento en forma de cadena que especifica un formato que puede constar de directivas.

Una directiva es una cadena que consta del carácter % (porcentaje) y 
una letra minúscula o mayúscula. Por ejemplo, la directiva %Y significa 
el año con el siglo como número decimal. Veámoslo en un ejemplo. Ejecuta 
el código en el editor.'''

from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

'''%Y: devuelve el año con el siglo como número decimal. En nuestro ejemplo, esto es 2020.
%m: devuelve el mes como un número decimal con relleno de ceros. En nuestro ejemplo, es 01.
%d: devuelve el día como un número decimal con relleno de ceros. En nuestro ejemplo, es 04.'''

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

'''El primero de los formatos utilizados se refiere solo al tiempo. 
Como puedes adivinar, %H devuelve la hora como un número decimal con 
relleno de ceros, %M devuelve el minuto como un número decimal con 
relleno de ceros, mientras que %S devuelve el segundo como un número 
decimal con relleno de ceros. En nuestro ejemplo, %H se reemplaza por 14, 
%M por 53 y %S por 00.'''

import time #<-- OBSERVA QUE ES EL MODULO TIME no MODULO DATETIME
# en este caso la funcion strftime además del argumento de formato, también puede tomar (opcionalmente) un objeto tuple o struct_time
timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

'''En la primera llamada a la función, formateamos el objeto struct_time, mientras que en la segunda llamada 
(sin el argumento opcional), formateamos la hora local. Puede encontrar todas las directivas disponibles en 
el módulo time'''

#método strptime()
#crea un objeto datetime a partir de una cadena que representa una fecha y una hora.

from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

'''Nota: En el módulo time, puedes encontrar una función llamada strptime, que analiza una cadena que representa 
un tiempo en un objeto struct_time. Su uso es análogo al método strptime en la clase datetime:'''

import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

#----------------
#Operaciones de fecha y hora
'''Para crear un objeto timedelta, simplemente realiza una resta en los objetos date o datetime, 
tal como hicimos en el ejemplo en el editor.'''
from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

#----------
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)

'''Por supuesto, también puedes crear un objeto tu mismo. 
Para ello, vamos a familiarizarnos con los argumentos aceptados por el constructor de la clase, 
que son:days, seconds, microseconds, milliseconds, minutes, hours, y weeks. Cada uno de ellos 
es opcional y el valor predeterminado es 0.

Los argumentos deben ser números enteros o de punto flotante, y pueden ser positivos o negativos.'''

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Días:", delta.days)
print("Segundos:", delta.seconds)
print("Microsegundos:", delta.microseconds)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)
