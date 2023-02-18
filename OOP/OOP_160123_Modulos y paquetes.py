#Se pueden importar los módulos en una misma línea de la sig forma:
import random, math
#O por separado de la siguiente forma:
import random  #para generar números aleatorios
import math #generar modelo matemático

import os, sys #módulos de sistemas

#-------------- 

print (math.ceil(1.2426)) #hace redondeo hacia el número mayor

from math import factorial #del módulo importa la entidad/función factorial
print (math.factorial(5)) # si no se importan de la forma de arriba se debe especificar del módulo del que viene
print (factorial (5)) #si se importa como se observa en la línea 22 entonces ya no es necesario especificar el módulo

print (random.randint(3,5)) #izquierda y derecha incluyentes en el rango

import math as m
from math import ceil
from math import floor
print (ceil (5.66)) #como se ha importado no es necesario especificar el módulo
print (floor(5.66)) 

print (m.cos(25)) #al especificar el alias del módulo se puede utilizar para invocar otras funciones 
#que no se han importado previamente "m" en vez de "math"

from math import sin, pi #importar varias entidades / funciones del mismo módulo
print (sin(pi/2))

import platform
from platform import platform

print (platform()) 
print (platform (1))
print (platform(0,1))

from platform import machine
print (machine()) #indica el nombre genérico del procesador

from platform import processor
print (processor()) #nombre real del procesador 

from platform import system

print(system()) #nombre genérico del sistema

#libreria OS
import os
dir (os) #muestra las entidades del módulo os

pip install matplotlib 
#se debe realizar dentro de la terminal en VS
#en GoogleCollab se puede ingresar el mismo código y es correcto


import matplotlib.pyplot as plt
import numpy as np

#hacer la data
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2,7, len(x))

#plot
fig, ax =plt.subplots()

ax.bar(x, y, widht=1, edgecolor = "white", linewidht=0.7)
ax.bar(x)

ax.set(xlim=(0,8), xticks=np.arange(1,8),
    ylim=(0,8), yticks=np.arange(1,8))

plt.show()






    



