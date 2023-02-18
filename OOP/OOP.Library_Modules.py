import random, math   
#Importa módulos
#random es para generar números aleatorios
#math es para generar modelos matemático

print(math.ceil(3.1416))
#se debe especificar el módulo al que pertence la entidad
#ceil hace redondeo hacia arriba

import math as m #Se le asignó un alias al módulo Se le denomina aliasing o renombrado
'''Nota: después de la ejecución exitosa de una importación con alias, el 
nombre original del módulo se vuelve inaccesible y no debe ser utilizado.'''
from math import factorial
from math import ceil
from math import floor
from math import * 
#El asterisco importa todas las entidades del módulo indicado
'''¿Es inseguro? Sí, a menos que conozcas todos los nombres proporcionados por el módulo, 
es posible que no puedas evitar conflictos de nombres. 
Trata esto como una solución temporal e intenta no usarlo en un código regular'''

#si se importan las entidades específicas no se
#tiene que específicar el módulo del que proviene la entidad

print (factorial(5))
print (ceil(5.66))
print (floor(5.66))

'''Si no se especifican y se agrega un alias
se puede hacer referencia al módulo con su alias y la entidad'''

print (m.factorial(5))


