line = input("Ingresa una línea de números, separalos con espacios")
strings = line.split()
print(strings)
total=0 #var en donde se realizará la suma
try:
    for substr in strings:
        total += float(substr) #aquí se está conviertiendo de str a float
    print ('El total es: ', total)
except:
    print(substr, "no es un numero")
 