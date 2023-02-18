x = str(input("Ingresa los números del 1-0 que quieres observar en tu display: "))
'''La forma en la que la consola imprime la información es renglón por renglón, para que se puedan
observar en la terminal los números horizontalmente, entonses se tiene que ingresar el código renglón por renglón,
se guarda un renglón por lista'''

display1 = [' ### ', ' # ', ' ### ', ' ### ', ' # # ', ' ### ', ' ### ', ' ### ', ' ### ', ' ### ']
display2 = [' # # ', ' # ', '   # ', '   # ', ' # # ', ' #   ', ' #   ', '   # ', ' # # ', ' # # ']
display3 = [' # # ', ' # ', ' ### ', ' ### ', ' ### ', ' ### ', ' ### ', '   # ', ' ### ', ' ### ']
display4 = [' # # ', ' # ', ' #   ', '   # ', '   # ', '   # ', ' # # ', '   # ', ' # # ', '   # ']
display5 = [' ### ', ' # ', ' ### ', ' ### ', '   # ', ' ### ', ' ### ', '   # ', ' ### ', ' ### ']

for i in x:
    print(display1[int(i)], end='') #[int(i)] #se refiere al índice
print() #se agrega para especificar el enter en la impresión de los caracteres
for i in x:
    print(display2[int(i)], end='') 
print()
for i in x:
    print(display3[int(i)], end='') 
print()
for i in x:
    print(display4[int(i)], end='') 
print()
for i in x:
    print(display5[int(i)], end='') 
print()

 




