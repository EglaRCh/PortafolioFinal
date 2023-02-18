import math
from math import pow, sqrt
a = int (input("Ingresa el valor de la variable a: "))
b = int (input("Ingresa el valor de la variable b: "))
x = int (input("Ingresa el valor de la variable x: "))
y = int (input("Ingresa el valor de la variable y: "))
ax = a * x
bx = b * x
ay = a * y
by = b * y
base_1 = ax - bx
base_2 = ay - by
potencia_1 = pow(base_1, 2)
potencia_2 = pow(base_2, 2)
base_sqr_1 = potencia_1 + potencia_2
D = sqrt(base_sqr_1)

print ("D = ((AX - BX)^2 + (AY - BY)^2)^-2 = ", D)
