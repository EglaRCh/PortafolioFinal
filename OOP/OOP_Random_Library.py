import random 
#¿Quién comienza?
#Generar un aleatorio ya sea 0 o 1 (Inicio, Final)
comienza = random.randint(0,1) 
#randint busca aleatoriamente numeros enteros dentro del 
# intervalo especificado (primer numero del intervalo, ultimo numero del intervalo)
while True:
    comienza = random.randint (0,1)
    print ("El número obtenido es: ", comienza)
    if comienza == 0:
        print ("Comienza el jugador 1")
    else:
        print("Comienza el jugador 2")
    continuar = input("Desea continuar (Si(S) /No (N))? ")
    if continuar == "N" or continuar == "n":
        break

print ("Muchas gracias")
#---------------
continuar = input("Desea continuar (Si(S) /No (N))? ")
print ( "Mayus: ", continuar.upper())
print ( "Minus: ", continuar.lower())

#---------------

x = 1 
#x es la cantidad de veces que se va a repetir el while y se especifica que comience en 1
n1 = 0 #numero de comienzo para el conteo
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0

#WHILE
while (x <= 10):
    numero = random.randint(1,6) #intervalo
    print ("El número ontenido es: ", numero)

    if numero == 1:
        n1 = n1 + 1
    elif numero == 2:
        n2 = n2 + 1
    elif numero == 3:
        n3 = n3 + 1
    elif numero == 4:
        n4 = n4 + 1
    elif numero == 5:
        n5 = n5 + 1
    else: 
        n6 = n6 + 1

    x = x + 1 #Variable acumulativa

    #impresion del número de veces que salió un dígito
    print ("El número de veces que salio 1 son: ", n1)
    print ("El número de veces que salio 1 son: ", n2)
    print ("El número de veces que salio 1 son: ", n3)
    print ("El número de veces que salio 1 son: ", n4)
    print ("El número de veces que salio 1 son: ", n5)
    print ("El número de veces que salio 1 son: ", n6)

    #-------------------

    #ciclo que se ejecuta 10 veces FOR
    for x in range (10):
        #Genera un número aleatorio entre el 1 y el 6
        numero = random.randint (1,6)
        print ("El número obtenido es: ", numero)
        #Evalua que numero salio
        if numero == 1: 
            n1 = n1+1
        elif numero == 2:
            n2 = n2+1
        elif numero == 3:
            n3 = n3 + 1
        elif numero == 4:
            n4 = n4 + 1
        elif numero == 5:
            n5 = n5 + 1
        else: 
            n6 = n6 + 1

#-------------

frutas = ['pera', 'manzana', 'plátano', 'ciruela']
for i in range (3):
    print ("Fruta seleccionada:", random.choice (frutas))
#random.choice seleccionar elementos aleatoreamente

baraja = [1,2,3,4,5,6,7,8,9,10,11,12,13,100]
print ("Baraja inicial: ", baraja)
for i in range (3):
    random.shuffle (baraja)
    print("Baraja movida: ", baraja)
#shuffle : revolver algo
baraja = ["El valiente", "El arpa", "el bandolon", "El jinete"]
print ("Baraja inicial: ", baraja)
for i in range (3):
    random.shuffle(baraja)
    print("Baraja movida: ", baraja)