#a)
'''e = int(input("Ingresa el número de existencias: "))
if e < 1000:
    print("Solicitar STOCK")
else:
    print("STOCK suficiente")'''

#b)
'''x = int(input("Ingresa un número aleatorio: "))
y = int(input("Ingresa un número aleatorio: "))
z = int(input("Ingresa un número aleatorio: "))

if x == y == z:
    print("Todos los números son iguales")
else:
    print("Los números son diferentes")

print("Los números ingresados son: ", x, ",", y, ",", z)'''

'''#c)
print ("Régimen", "HONORARIOS", sep=("\n"))
dprmnt = str(input("Ingrese el Departamento: "))
laborhrs = int(input("Ingresa el total de horas trabajadas al mes: "))
admin = int(3_500)
systems = int(8_000)
acctcy = int(12_000)
markting = int(8_000)
hradmin = admin/160
hrsystems = systems/160
hracctcy = acctcy/160
hrmarkting = markting/160
 
if dprmnt == "Administracion" :
    print("hora admin: ", hradmin)
    hono = hradmin * laborhrs
    iva = hono * 0.16
    subT = hono + iva
    rISR = hono * 0.10
    rIVA = hono * 0.10
    neto = subT - rISR - rIVA

if dprmnt == "Sistemas" :
    print("hora sistemas: ", hrsystems)
    hono = hrsystems * laborhrs
    iva = hono * 0.16
    subT = hono + iva
    rISR = hono * 0.10
    rIVA = hono * 0.10
    neto = subT - rISR - rIVA

if dprmnt == "Contabilidad" :
    print("hora contabilidad", hracctcy)
    hono = hracctcy * laborhrs
    iva = hono * 0.16
    subT = hono + iva
    rISR = hono * 0.10
    rIVA = hono * 0.10
    neto = subT - rISR - rIVA

if dprmnt == "Mercadotecnia" :
    print("hora mercadotecnia: ", hrmarkting,)
    hono = hrmarkting * laborhrs
    iva = hono * 0.16
    subT = hono + iva
    rISR = hono * 0.10
    rIVA = hono * 0.10
    neto = subT - rISR - rIVA

print("Neto: ", neto)

if neto > 1800:
    print("La Base de Impuestos es mayor")
else:
    print("La Base de Impuesto es menor")'''

a = float(input("Ingresa un cateto (lado) del triángulo: "))
b = float(input("Ingresa otro cateto (lado) lado del triángulo: "))
c = float(input("Ingresa la hipotenusa del triángulo: "))

if a == b and b == c and c == a :
    print("El triángulo es equilátero")

if a == b and b != c or b == c and c != a or a == c and b != a :
    print("El triángulo es isóceles")

if a != b and b != c and c != a :
    print("El triángulo es escaleno")


