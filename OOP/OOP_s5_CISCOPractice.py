'''''class TheSimplestClass :
    pass
variable = TheSimplestClass ()'''

'''La pila: enfoque procedimental'''
'''stack = [] #Stack es igual a una lista vacía

def push (val) : #función que en su parámetro acepta el valor que agregará al final de la lista stack
    stack.append(val)

def pop () : #la función toma el último valor de la fila, lo elimina y al final lo muestra
    val = stack[-1] #asignación del último valor de la fila en la variable val
    del stack [-1] #eliminación del último valor de la fila
    return val #muestra el valor guardado previamente en la variable val

push(3)
push(2)
push(1)

print(pop()) #1
print(pop()) #2
print(pop()) #3'''''

'''La pila: enfoque orientado a objetos'''
class Stack:
    def __init__ (self):
        self.__stack_list = [] #ENCAPSULAMIENTO al colocar dos guines bajos la propiedad se vuelve privada

    def push (self, val): #tienen más parámetros que sus contrapartes procedimentales
        self.__stack_list.append(val)
    
    def pop (self): #tienen un parámetro self. Todos los métodos deben tenerlo, desempeña el papel constructor
        #permite que el método acceda a entidades (propiedades y actividades/métodos) del objeto
        val = self.__stack_list [-1]
        del self.__stack_list [-1]
        return val
'''
stack_object = Stack()
stack_object_1=Stack()
stack_object_2=Stack()

#print(len(stack_object.stack_list)) #Genera un AttributeError

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop()) #3

print(stack_object_2.pop())
print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

little_stack = Stack()
another_stack = Stack()
funny_stack =  Stack ()

little_stack.push(1)
another_stack.push(little_stack.pop()+1)
funny_stack.push(another_stack.pop()-2)

print(funny_stack.pop())'''

class AddingStack (Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    def push (self, val):
        self.__sum += val
        Stack.push(self, val)
    def pop(self):
        val = Stack.pop (self)
        self.__sum -= val
        return val
    def get_sum(self):
        return self.__sum #Devuelve la variable que se enceuntra privada, sólo la muestra
    
stack_object = AddingStack ()

for i in range (100):
    stack_object.push (i)
print (stack_object.get_sum())

'''for i in range (5):
    print (stack_object.pop())'''

class ExampleClass:
    def __init__(self, val=1):
        self.first = val
    def set_second(self, val):
        self.second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__) #{'first': 1}
 #uno de los métodos predefinidos pertenecientes a los objetos es __dict__ (un diccionario)
print(example_object_2.__dict__) #{'first': 2, 'second':3}
#al  solicitar el métoro, arroja el nombre en el diccionario con su significado
print(example_object_3.__dict__) #{'first': 4, 'third':5}

class ExampleClass2:
    def __init__(self, val=1):
        self.__first = val
    def set_second(self, val):
        self.__second = val

example_object_1_2 = ExampleClass2()
example_object_2_2 = ExampleClass2(2)

example_object_2_2.set_second(3)

example_object_3_2 = ExampleClass2(4)
example_object_3_2.third = 5

print(example_object_1_2.__dict__) 
print(example_object_2_2.__dict__) 
print(example_object_3_2.__dict__)

#Variable de clase

class ExampleClass3:
    counter = 0 #Variable de clase
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1 

example_object_1_3 = ExampleClass3()
example_object_2_3 = ExampleClass3(2)
example_object_3_3 = ExampleClass3(4)

print (example_object_1_3.__dict__, example_object_1_3.counter) #{'_ExampleClass__first': 1} 3
print (example_object_2_3.__dict__, example_object_2_3.counter) #{'_ExampleClass__first': 2} 3
print (example_object_3_3.__dict__, example_object_3_3.counter) #{'_ExampleClass__first': 4} 3

#mètodo __dict__ para la variable de clase
class ExampleClass4:
    varia = 1 #variable de clase
    def __init__(self, val):
        ExampleClass4.varia = val #si se especifica self.varia=val se convertiría en variable de instancia, como se escribió permanece como variable de clase


print(ExampleClass4.__dict__) #arroja la dirección con el valor de la vvariable = 1
example_object = ExampleClass4(2)

print(ExampleClass4.__dict__) #arroja la dirección con el valor = 2
print(example_object.__dict__) #muestra un diccionario vacío porque el objeto no tiene variables de instancia
  
'''class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1'''  #.a no está definido como atribudo en el constructor, no se puede acceder a ella

        
#como manejar un AttributeError, es decir, un atributo no declarado en el construtcot: con hasattr
class ExampleClass5:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass5(1)
print(example_object.a)

if hasattr(example_object, 'b'):
    print(example_object.b)

class ExampleClass6:
    attr = 1


print(hasattr(ExampleClass6, 'attr')) #True
print(hasattr(ExampleClass6, 'prop')) #False

class ExampleClass7:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass7()

print(hasattr(example_object, 'b')) #True sí contiene la variable b el objeto que contiene la clase
print(hasattr(example_object, 'a')) #True '  '
print(hasattr(ExampleClass7, 'b')) #False, la calse no contiene la variable b solo la a
print(hasattr(ExampleClass7, 'a')) #True, la clase sí contiene la variable a

#Métodos a detalle
class Classy:
    def method (self):
        print("método") #un método es una función que está dentro de una clase
        #el método está obligado a tener al menos un parámetro
        #NO existen métodos sin parámetros
        #Un método puede invocarse sin un argumento, pero on puede declararse sin parámetros
        #primer (o único) parámetro se denomina self
        #el nombre self identifica el objeto para el cual se invoca el método
obj =  Classy() #se trata al nombre de la clase como una función
obj.method() #devuelve un objeto recien instaciado de la clase.

'''Si deseasque el método acepte parámetros distintos a self
debes:
Colocarlos DESPUES de self en la definición del método
Pasarlos como ARGUMENTOS durante la invocación sin especificar self'''

class Classy1:
    def method (self, par):
        print ('método:', par)

obj = Classy1
obj.method(1) #método:1
obj.method(2)#método:2
obj.method(3)#método:3

#Parámetro self
#Es usado para obtener acceso a la instancia del objeto
#y a las variables de clase

class Classy2:
    varia = 2 #variable de clase
    def method(self):
        print(self.varia, self.var)


obj = Classy2()
obj.var = 3 #asigna un valor a la variable de instancia
obj.method() #realiza la acción del método

#self: también se usa para invocar otros métodos desde dentro de la clase
class Classy3:
    def other (self):
        print('otro')
    def method(self):
        print('método')
        self.other()

obj=Classy3()
obj.method()

#__init__
#Si se nombra un método de esta manera:
#__init__, no será un método degular, será un CONSTRUCTOR
#Si una clase tiene un constructor, este se invoca automáticamente
#e implícitamente cuando se instancia el objeto de la clase

'''El SONTRUCTOR
Está obligado a tener el parámetro self (se configura automáticamente)
Pudiera (pero no necesariamente) tener más parámetros que solo self; si esto sucedem
la forma en que se usa el  nombre de la clase para crear el objeto debe tener la definición __init__
Se puede utilizar para configurar el objeto, es decir, inicializa adecuadamente su estado interno, crea variables
de instancia, crea instancias de cualaquier otro objeto si es necesario, etc.

Ten en cuenta que el CONSTRUCTOR:
No puede retornar un valor, ya que está diseñado para devolver un OBJETO recién creado y nada más
No se puede invocar directamente desde el objeto o desde dentro de la clase (puedes invocar un constructor
desde cualquier de las superclases del objeto)'''

class Classy3:
    def __init__ (self, value):
        self.varx = value

obj_1 = Classy3("objeto")
print (obj_1.varx)

#__init__ es un método, y un método es una función, puedes hacer los mismos trucos con constructores
#y métodos que con las funciones ordinarias
#Ejemplo:
class Classy4:
    def __init__ (self, value = None):
        self.varxx = value

obj_1 = Classy4 ('objeto')
obj_2 = Classy4 ()

print (obj_1.varxx) #imprime el método
print (obj_2.varxx)

#Con los métodos también aplica cuando se colocan dos guines bajos __ esta (parcialmente) oculto
class Classy5:
    def visible(self):
        print('visible')

    def __hidden(self):
        print('oculto')
obj = Classy5()
obj.visible()

try:
    obj.__hidden()
except:
    print('fallido')

obj._Classy5__hidden()

#cada CLASE y OBJETO de Python está pre-equipado
#con un conjunto de atributos útiles que pueden usarse
#para examinar sus capacidades

#__dict__ en la clase. 

class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__) #{'var': 2}
print(Classy.__dict__) #{'__module__': '__main__', 'varia': 1, '__init__': <function Classy.__init__ at 0x7f952943f320>, 'method': <function Classy.method at 0x7f952943f3b0>, '_Classy__hidden': <function Classy.__hidden at 0x7f952943f440>, '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objects>, '__doc__': None}

#Otra propiedad incorporada, al conjunto incorporado a objetos y clases, es una cadena llamada __name__.
#__name__ contiene el nombre de la clase 
#NOTA: el atributo __name__ está ausente del objeto, existe solo dentro de las clases

#Para encontrar la clase de un OBJETO en particular, --> función type(), entre otras cosas, encuentra una clase que se haya utilizado para crear instancias de cualquier objeto

class Classy6:
    pass
print(Classy6.__name__)#Classy6
obj = Classy6() 
print(type(obj).__name__) #Classy6
#print(obj.__name__) #Causa un error

#__module__ es una cadena, también ALMACENA EL NOMBRE 
#DEL MODULO QUE CONTIENE LA DEFINICION DE LA CLASE

#Cualquier módulo llamado __main__ en realidad NO ES UN MODULO
#sino, ES EL ARCHIVO ACTUALMENTE EN EJECUCIÓN
class Classy:
    pass


print(Classy.__module__) #__main__
obj = Classy()
print(obj.__module__) #__main__

#__bases__ ES UNA TUPLA. La TUPLA CONTIENE CLASES (no nombres de clases)
#que son superclases directas de la clase

#NOTA: solo las clses tienen este atributo, los objetos no

class SuperOne:
    pass
class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass

def printBases(cls):
    print('(', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')

printBases(SuperOne) #( object )
printBases(SuperTwo) #( object )
printBases(Sub)      #( SuperObe SuperTwo )

#Nota: una clase sin superclases explícitas apunta a object 
# (una clase de Python predefinida) como su antecesor directo.

#REFLEXIÓN E INTROSPECCIÓN
'''El programador de Pythonrealiza dos actividades importantes específicas para muchos
lenguajes objetivos. Las cuales son:
Introspección, capacidad de un programa para examinar el tipo o las propiedades de un objeto
en tiempo de ejecución
Reflexión, va un paso más allá, es la capacidad de un programa para manipular los valores,
propiedades y/o funciones de un objeto en tiempo de ejecución
En otras palabras, no tienes que conocer la definción completa de clase/objeto para manipular
el objeto, ya que el objeto y/o su clase contienen los metadatos que te permiten reconocer sus 
características durante'''

#Qué puedes descubrir acerca de las clases en Python?
#Todo
#Tanto la introspección como la reflexión permite al proframador
#hacer cualquier cosa con cada objeto, sin importar de dónde provenga

class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI (obj):
    for name in obj.__dict__.keys() : #escanea el atributo __dict__, buscando todos los nombres de atributos
        if name.startswith ('i') : #si un nombre comienza con 'i'
            val = getattr (obj, name) #getatrr() toma dos argumentos: un objeto y su nombre de propiedad (como una cadena) y devuelve el valor del atributo actual
            if isinstance (val, int) : #revisa si el primer argumento es del tipo del segundo argumento
                setattr (obj, name, val +1) #asigna al valor del atributo seleccionado del objeto especificado en el tercer argumento

print(obj.__dict__) #{'a': 1, 'integer': 4, 'b': 2, 'i': 3, 'z': 5, 'ireal': 3.5}
incIntsI(obj) #{'a': 1, 'integer': 5, 'b': 2, 'i': 4, 'z': 5, 'ireal': 3.5}
print(obj.__dict__)

#getatrr()
'''class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'age')'''
 
#setattr(object, attribute, assignedvalue)

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    
    def __str__(self):
        return self.name + 'en' +self.galaxy

sun = Star('Sol', 'vía Lactea')
print (sun) #sólo arroja la dirección del objeto si no contiene el método ___str__()

#Para que una clase u objeto deba ser presentado como una cadena,
#intenta invocar un método llamado __str__() del objeto y emplear la cadena que devuelve

'''La herencia_ pasar atributos y métodos de la superclase
(definida y existente) a una clase recién creada, llamada subclase 
es una forma de construir una nueva clase, no desde cero, sino 
utilizando un repertorio de rasgos ya definido
la nueva clase hereda (y esta es la clave) todo 
todo el equipamiento ya existente, pero agregar algo nuevo si es necesario
Por lo anterior es posible construit clases más especializadas (mas concretas)'''

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t") #issibclass() revisa si el PRIMER argumento es una subclase del SEGUNDO y devuelve True o False
    print()

#un objeto es la encarnación de una clse
#¿Cómo saber si un objeto es de cierta clase o no?
#con la funcipon isinstance():
#isinstance(objectName, ClassName) Devuelve True si el objeto es una instancia de la clase,
#o False de lo contrario
'''Si una subclase contiene al menos las mismas características que cualquiera de la superclase
pueden hacer lo mismo que los objetos derivados de la superclase, por lo tanto, es una instancia 
de su clase de inicio y cualquiera de sus superclases'''

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()

#El OPERADOR is verifica si dos variables, se refieren al mismo objeto
#RECUERRDA: las variables NO almacenan los objetos en sí, sino solo los
#identificadores que apuntan a la memoria interna de Python

class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2) #False
print(object_2 is object_3) #False
print(object_3 is object_1) #True
print(object_1.val, object_2.val, object_3.val) #1 2 1

string_1 = "Mary tenía un "
string_2 = "Mary tenía un corderito"
string_1 += "corderito"

print(string_1 == string_2, string_1 is string_2) #True False

#¿Cómo Python trata con los métodos de herencia?

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Mi nombre es " + self.name + "."

class Sub(Super): #hereda todos las propiedades de la superclase
    def __init__(self, name):
        Super.__init__(self, name)

obj = Sub("Andy")
print(obj) #Mi nombre es Andy

#LA FUNCIÓN super (), accede a la superclase sin neecsidad de conocer su nombre:
#super().__init__(name)

'''La función super() crea un contexto en el que no tiene que pasar
el argumento proío al método que se invoca, es por eso que es posible
activar el constructor de la superclase utilizando solo un argumento.
NOTA: puedes usar este tanto para invocar al constructor de la superclase,
como para obtener acceso a cualquiera de los recursos disponibles dentro de
la superclase'''

class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Mi nombre es " + self.name + "."

class Sub(Super) :
    def __init__ (self,name):
        super() .__init__(name)

obj = Sub("Andy")
print(obj)

# Probando propiedades: variables de clase.
class Super:
    supVar = 1

class Sub(Super):
    subVar = 2

obj = Sub()
print(obj.subVar) #2
print(obj.supVar) #1

# Probando propiedades: variables de instancia.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar) #12
print(obj.supVar) #11

class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())

#100 101 102
#200 201 202
#300 301 302

'''cuando intentas acceder a una entidad de cualquier objeto,
Python intentará en este orden
Encontrarla dentro del objeto mismo
Encontrarla en todas las clases involucradas en la línea de herencia
del objeto de abajo hacia arriba
Si ambos intentos falllan, una excepción (AttributeError) será generada'''

#Herencia Múltiple
#Ocurre cuando una clase tiene más de una superclase relacionada


class SuperA:
    var_a = 10
    def fun_a(self):
        return 11


class SuperB:
    var_b = 20
    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()

print(obj.var_a, obj.fun_a()) #10 11
print(obj.var_b, obj.fun_b()) #20 21

#overriding (anulación) ¿Qué sucederá si más de una de las superclases define una entidad con un nombre en particular?
class Level1:
    var = 100
    def fun(self):
        return 101

class Level2(Level1):
    var = 200
    def fun(self):
        return 201

class Level3(Level2):
    pass

obj = Level3()

print(obj.var, obj.fun())

'''Tanto la clase, Level1 y Level2 definen un método llamado fun() 
y una propiedad llamada var. ¿Significará esto el objeto de la 
claseLevel3 podrá acceder a dos copias de cada entidad? 
De ningún modo.'''
'''La entidad definida después (en el sentido de herencia) 
anula la misma entidad definida anteriormente.'''

class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"

class Sub(Right, Left): #R LL RR Right si el orden es Right Left, si es Left Right el resultado es: L LL RR Left
    pass

obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())

#Python busca componentes de objetos en el siguiente orden:
#Dentro del objeto mismo
#En sus superclases, de abajo hacia arriba
#Si hay más de una clase en una herencia, Python las escanea de izquierda a derecha

'''Cómo construir una jerarquía de clases'''
class One:
    def do_it(self):
        print("do_it de One")

    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("do_it de Two")


one = One()
two = Two()

one.doanything()
two.doanything()

'''Nota: la situación en la cual la subclase 
puede modificar el comportamiento de su superclase 
(como en el ejemplo) se llama poliformismo. 
La palabra proviene del griego (polys: "muchos, mucho" y morphe, 
"forma, forma"), lo que significa que una misma clase puede tomar 
varias formas dependiendo de las redefiniciones realizadas por 
cualquiera de sus subclases.
El método, redefinido en cualquiera de las superclases, 
que cambia el comportamiento de la superclase, se llama virtual.'''

import time

class Vehicle:
    def change_direction(left, on):
        pass

    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)


class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass

    def change_direction(left, on):
        control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(left, on):
        turn_front_wheels(left, on)

#La composición es el proceso de componer un objeto
#usanto otros objetos diferentes
#Los objetos utilizando en la composición entregan un conjunto de rasgos deseados
#(propiedades y/o metodos), podemos decir que actúan como bloques utilizados para construir
#una estructura más complicada

'''La herencia extiende las capacidades de una clase
agregando nuevos componentes y modificando los existentes;
en otras palabras, la receta completa está contenida dentro 
de la clase misma y todos sus ancesotros; el objeto toma todas 
las pertenencias de la clase y las usa
La composición proyecta una clase como conetenedor capaz de almacenar 
y usar otros objetos (derivados de otras clases) donde cada uno de los objetos 
implementa una parte del comportamiento de una clase'''

import time

class Tracks:
    def change_direction(self, left, on):
        print("pistas: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("ruedas: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels()) #objeto compuesto por otros objetos COMPOSICION
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)

'''ruedas:  True True
pistas:  True False
tracks:  False True
tracks:  False False'''

#no entiendo el código

'''En la herencia simple y múltiple no hay obstáculos, solo hay un PERO, el que puedas
no significa que tengas que:
Una sola clase de herencia siempre es más simple, segura y fácil de entender y mantener
La herencia múltimple siempre es arriesgada, ya que tienes muchas oportunidades de cometer 
un error al identificar estas partes de las super clases que influirán efectivamente en la nueva clase
La herencia múltimple puede hacer que la anulación sea extremadamente difósil; además,
el emplear la función super() se vuelve ambiguo
La herencia múltiple viola el principio de responsabilidad únida https://en.wikipedia.org/wiki/Single_responsibility_principle
ya que forma una nueva clase de dos o más clases que no saben nada una de la otr
Sugerimos la herencia múltiple como la última de todas las posibles soluciones:
si relamente necesitas diferentes clases, la COMPOSICION puede ser una mejor alternativa'''

#ORden de Resolución de Métodos (MRTO) es una ESTRATEGIA
#En la que el lenguaje de programación en particular escanea 
#la parte superior de la jerarquía de una clase para encontrar el método 
#que necesita actualmente.
#LOS DIFERENTES LENGUAJES usan MROs LEVEMENTE o completamente DIFERENTES
#Cuando se hacen herencias múltiples en Python y se asignan las superclases a la subclase
#diferente a cómo está escrito en el código se arroja un TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle

#ejemplo
'''class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Top, Middle): <-- La herencia se escribe en desorden al código previo
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

''' #TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle

#otro problema que puede surgir en las herencias multiples
#El problema del diamante
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

'''Java y C+ no permiten la herencia multiple
EN Python sí es posible, pero no olvides que el MRO está a cargo'''

class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Right, Middle_Left): #Si se cambia el orden de la herencia, como estan en la misma jerarquía de subclases sí es posible, entonces el resultado devolverá el método de la primer superclase escrita en los atributos de la subclase
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

'''. Para encontrar cualquier propiedad de objeto/clase, Python la busca dentro:

Del objeto mismo.
Todas las clases involucradas en la línea de herencia del objeto de abajo hacia arriba.
Si existe más de una clase en una ruta de herencia en particular, Python las escanea de izquierda a derecha.
Si lo mencionado anteriormente falla, la excepción AttributeError es generada.


8. Si alguna de las subclases define un método, variable de clase o variable de instancia del mismo nombre 
que existe en la superclase, el nuevo nombre anula cualquiera de las instancias anteriores del nombre. '''

'''try:
    except:
    else: <-- ejecutará siempre que se haya generado una excepcion
    finally: <-- Siempre se ejecuta, sin importar lo sucedido antes'''

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
        return n
    finally:
        print("Es momento de decir adiós")
        return n

print(reciprocal(2)) #Todoo salio bien
print(reciprocal(0)) #Division fallida

#las excepciones son clases
#cuando se genera una excepcion, se crea una instancia
#de un objeto de la clase y pasa por todos los niveles 
#de ejecución del programa, buscando el bloque 'except'
#que esta preparado para tratar con la excepcion
 try:
    i = int("¡Hola!")
except Exception as e:
    print(e)
    print(e.__str__())

'''Nota: el alcance del identificador solo es dentro del except
y no va mpas alla'''

'''Todas las excepciones integradas de Python formal una jerarquía de clases
se puede extender sin problema
Como un arbol es un ejemplo perfecto de una estructura de datos recursiva. Larecursion
parace lamejor manera de recorrerlo '''

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)

#Hay algunas imprecisiones sutiles en la forma en que se presentan algunas ramas

def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ') # :  :
    print_args(e.args)

try:
    raise Exception("mi excepción")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ') #mi excepción : mi excepción : mi excepciín
    print_args(e.args)

try:
    raise Exception("mi", "excepción")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ') #('mi', 'excepción') : ('mi', 'excepción') : ('mi', 'excepción')
    print_args(e.args)

'''Definir tus propias excepciones como subclases derivadas
de las predefinidas '''

class MyZeroDivisionError(ZeroDivisionError):	
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("peores noticias")
    else:		
        raise ZeroDivisionError("malas noticias")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('División entre cero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('Mi división entre cero')
    except ZeroDivisionError:
        print('División entre cero original')

#cómo crear tu propia excepcion
class PizzaError(Exception):
    def __init__(self, pizza='desconocida', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='desconocida', cheese='>100', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError
    if cheese > 100:
        raise TooMuchCheeseError
    print("¡Pizza lista!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

#puntos Clave
'''1. El bloque else: de la sentencia try se ejecuta cuando no ha habido ninguna excepción durante la ejecución del try:.


2. El bloque finally: de la sentencia try es siempre executado.


3. La sintaxis except Exception_Name as exception_object: te permite interceptar un objeto que contiene información sobre una excepción pendiente. La propiedad del objeto llamada args (una tupla) almacena todos los argumentos pasados al constructor del objeto.


4. Las clases de excepciones pueden extenderse para enriquecerlas con nuevas capacidades o para adoptar sus características a excepciones recién definidas.'''

