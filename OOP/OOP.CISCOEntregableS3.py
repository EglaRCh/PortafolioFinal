# Ejemplo 1
word = 'by'
print(len(word)) 
#len devuelve el número de caracteres que contiene el argumento
# Ejemplo 2
empty = ''
print(len(empty))
# Ejemplo 3
i_am = 'I\'m' 
#recuerda diagonal invertida es un carácter de escape
print(len(i_am))

#--------
#Cadenas multilínea
#El número delíneas de texto dentro de una cadena de 
#este tipo es arbitraria y se especifican con
#tres apóstrofes o tres comillas al inicio y al final
multiline = '''Línea #1
Línea #2''' #el caracter invisible es \n
#también funciona con """línea #1
# línea #2 """
print(len(multiline))

#------------
str1 = 'a'
str2 = 'b'
str2 += str1

print(str1 + str2) #el orden es relevante aquí
print(str2 + str1)
print(5 * 'a') #el orden no importa
print('b' * 4)
#https://www.freecodecamp.org/espanol/news/python-ejemplos-de-codigo-tutorial-de-programacion-en-python-desde-cero-para-principiantes/

#------------

#funcion ord()<- proveniente de ordinal: sirve para saber el valor del punto de código de 
#ASCII / UNICODE de un carácter específico

char_1 = 'a'
char_2 = ' '  # space
ch1 = 'α'
ch2 = 'ę'


print(ord(char_1)) #97
print(ord(char_2)) #32
print(ord(ch1)) #945
print(ord(ch2)) #281

#-------------
print(chr(97))  #a
print(chr(945)) #α

'''chr(ord(x)) == x
ord(chr(x)) == x 
El caracter del ordinal de x es x y el ordinal del caracter de x es x'''

#--------
'''Las cadenas pueden ser tratadas como listas
Por cada ix en el rango de la longitud de los caracteres de la variable 'the_string
imprime el caácter en el índice correspondiente al calor for ix y en cada final del 
ciclo agrega un espacio'''

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print() #s i l l y ...

#----------
#Slices o Rebanadas
alpha = "abdefg"

print(alpha[1:3]) #del índice 1 (incluyente) al 3(excluyente)
print(alpha[3:]) #desde el índice 3 (incluyente)
print(alpha[:3]) #hasta el índice 3 (excluyente)
print(alpha[3:-2]) #desde el índice 3 (incluyente) hasta el índice -2 (exc) considerando que el último los índices negativos comienzan en el final de los índices
print(alpha[-3:4])#desde el índice -3 (antepenultimo in) hasta el 4 (exc)
print(alpha[::2]) #desde el índice 0 (inc) : hasta el final : en saltos de 2 en 2 devolviendo el segundo caracter
print(alpha[1::2]) #desde el índice 1(inc):hasta el final:en saltos de 2 en 2 devolviendo el segundo caracter

#-----------
#Operadores in y not in REsultado: True o False
#in comprueba si el argumento izquierdo (una cadena) se puede encontrar en cualquier lugar del argumento derecho (una cadena)
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet) #true
print("F" in alphabet) #false
print("1" in alphabet) #false
print("ghi" in alphabet) #true
print("Xyz" in alphabet) #false

#not in si el argm. izq NO SE PUEDE ENCONTRAR en el derecho
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet) #False
print("F" not in alphabet) #True
print("1" not in alphabet) #True
print("ghi" not in alphabet) #False
print("Xyz" not in alphabet) #True

#-----------
#Las cadenas son inmutables
'''No todo lo que se puede hacer con una lista
se puede hacer con una cadena p.ej. no permite 
usar la instrucción del, append (), insert()
ejemplo
alphabet = 'abcd'
del alphabet [0] 
alphabet.append ("A")
alphabet.insert(0,"A")
No es permitido
Lo único que puedes hacer es eliminar la cadena 
como un todo'''

#--------
#Con operaciones se pueden modificar las cadenas
alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet #agrega la a al principio
alphabet = alphabet + "z" #agrega la z al final 

print(alphabet)

#operaciones con cadenas: min() Encuentra el valor mínimo de los puntos de código en la cadena
print(min("aAbByYzZ"))
print(ord(min("aAbBYyzZ"))) #A #recuerda que en la tabla ASCII las mayúsculas están asignadas con un punto de código con menor valor que las minúsculas

t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')
print(ord(min(t)))

y = [0, 1, 2]
# print(min(y)) #Arroja error porque es un valor de tipo int no str

#Operaciones con cadenas: max() Encuentra el valor máximo de los puntos de código de la secuencia
print(max("aAbByYzZ"))
print(ord(max("AabByYzZ")))

t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')
print(ord(max(t)))

t = [0, 1, 2]
print(max(t))
#print(ord(max(t))) #arroja error porque se pide el ord de un valor int no str

#Operaciones con cadenas:método index()<-No es una función Busca en la secuencia desde el principio, para encontrar 
# el primer elemento del valor especificado en su argumento
print("aAbByYzZaA".index("b")) #2
print("aAbByYzZaA".index("Z")) #7
print("aAbByYzZaA".index("A")) #1

#Operaciones con cadenas: la función list() Toma su argumento (una cadena)
#y crea una nueva lista que contiene todos los caracteres de la cadena, 
#uno por elemento de la lista
'''Nota: no es estrictamente una función de cadenas, es capaz de crear nuevas listas
de muchas otras entidades (ej. tuplas y diccionarios'''
print(list("abcabc")) #se convierte en lista ['a', 'b', 'c', ...]

#operaciones con cadenas: el método count() #Cuenta todas las apariciones del 
#elemento dentro de la secuencia. La ausencia del elemento no causa problema

print("abcabc".count("b")) #2 veces aparece 'b'
print('abcabc'.count("d")) #0 veces aparece 'd'

'''La lista completa de métodos exclusivos a procesar caracteres
se encuentra en el sig link: https://docs.python.org/3.4/library/stdtypes.html#string-methods.'''

print(len("\n\n")) #2 Los saltos de línea se contabilizan como 1 caracter

asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)

s = 'yesteryears'
the_list = list(s)
print(the_list[3:6]) #['t', 'e', 'r'] #al convertir la secuencia en una lista 
#el resultado es de la forma anterior


for ch in "abc":
    print(chr(ord(ch) + 1), end='') #este código le suma al punto de código un valor 
#y devuelve el caracter correspondiente al punto sumado

'''Métodos de cadenas'''
#Método capitalize() - capitalize:escribir con mayúsculas
#crea una nueva cadena con los caracteres tomados de la cadena fuente
#1.Si elprimer carácter dentro de la cadena es una letra, se convertirá a mayúsculas
#2.Todas las letras restantes de la cadena se convertirán en minúsculas

print('aBcD'.capitalize()) #Abcd
print("Alpha".capitalize()) #Alpha
print('ALPHA'.capitalize()) #Alpha
print(' Alpha'.capitalize()) # alpha
print('123'.capitalize())    #123
print("αβγδ".capitalize())   #Αβγδ

#No olvides que:
'''La cadena original desde la cual se invoca el 
método no se cambia de ninguna manera, la inmutabilidad de una 
cadena debe obedecerse sin reservas.
La cadena modificada (en mayúscula en este caso) se devuelve 
como resultado; si no se usa de alguna manera (asígnala a una variable 
o pásala a una función / método) desaparecerá sin dejar rastro.'''

#Método center()
#genera una copia de la cadena original, tratando de centrarla dentro
#de un campo de un ancho especificado
#el centralizado se realiza al agregar algunos espacios antes y después de la cadena

print('[' + 'alpha'.center(10) + ']') #[  alpha   ]
print('[' + 'Beta'.center(2) + ']')   #[Beta] #cuando la longitud del campo de destino es demasiado pequeña, se devuelve la cadena original
print('[' + 'Beta'.center(4) + ']')   #[Beta]
print('[' + 'Beta'.center(6) + ']')   #[ Beta ]

#La variante de dos parámetros de center() hace uso del carácter del segundo argumento, 
#en lugar de un espacio
print('[' + 'gamma'.center(20, '*') + ']') #[*******gamma********]

#Método endswith() 
#comprueba si la cadena dada termina con el argumento especificado y devuelve: True o False

if "epsilon".endswith("on"):
    print("si") #<- resultado
else:
    print("no")

t = "zeta"
print(t.endswith("a")) #True
print(t.endswith("A")) #False
print(t.endswith("et")) #False
print(t.endswith("eta")) #True

#El método find()
#busca una subcadena y devuelve el índice de la primera aparición
#de esta subcadena
#No genera un arror para un argumento que contiene una subcadena 
#inexistente (devuelve -1 en dicho caso)
#Funciona sólo conc cadenas
'''Nota: no se debe emplae find() si deseas verificar sólo un carácter
dentro de una cadena - el operador in es más rápido'''

print("Eta".find("ta")) #1
print("Eta".find("mma")) #-1
o = 'theta'
print(o.find('eta')) #2
print(o.find('et'))  #2
print(o.find('the')) #0
print(o.find('ha')) #-1

#método isalnum()
#comprueba si la cadena contiene sólo dígitos o caracteres alfabéticos (letras)
#y devuelve: True o False de acuerdo al resultado

'''Cualquier elemento de cadena que no sea un dígito o una letra
hace que el método regrese False. Una cadena vacía tmbn lo hace'''
print('lambda30'.isalnum()) #True
print('lambda'.isalnum())   #True
print('30'.isalnum())       #True
print('@'.isalnum())        #False
print('lambda_30'.isalnum())#False
print(''.isalnum())         #False

t = 'Six lambdas'
print(t.isalnum()) #False debido al espacio
t = 'ΑβΓδ'
print(t.isalnum()) #True
t = '20E1'
print(t.isalnum()) #True

#Método isalpha()
#sólo se interesa en letras.
print("Moooo".isalpha()) #True
print('Mu40'.isalpha())  #False

#Método isdigit()
#Al contrario, busca sólo dígitos, cualquier otra cosa produce False
print('2018'.isdigit()) #True
print("Year2019".isdigit()) #False

#Método islower() <- variante de isalpha()
#solo acepta letras minúsculas
print("Moooo".islower()) #False
print('moooo'.islower()) #True

#Método isspace()
#identifica espacios en blanco solamente.
print(' \n '.isspace()) #True
print(" ".isspace()) #True
print("mooo mooo mooo".isspace()) #False

#Método isupper()
#sólo se concentra en mayúsculas
print("Mooo".isupper()) #False
print("mooo".isupper()) #False
print('MOOO'.isupper()) #True

#Método join()
#realiza una unión, y espera un argumento de tipo lista 
#se debe asegurar que todos los elementos de la lista sean str o de lo contrario generará una excepción TypeError
#Todos los elementos de la lista serán unidos en una sola cadena pero
#La cadena desde la que se invoca el método será utilizada como separador,
#puesta entre las cadenas
#La cadena recién creada se devuelve como resultado

print(",".join(["omicron", "pi", "rho"])) #omicron,pi,rho

#Método lower ()
#genera una COPIA de una cadena, reemplaza todas las letras mayúsculas con sus equivalentes en minúsculas
#si la cadena original no contiene ca.mayúsculas, la cadena devuelve la original
print("SiGmA=60".lower()) #sigma=60


#Método lstrip()
#l<- left devuelve una cadena recién creada formada a partir de la original eliminando todos los espacios en blanco iniciales
print("[" + "     tau ".lstrip() + "]") #[tau ] #observa que sólo los espacios del principio se eliminaron, los posteriores se mantuvieron

print("www.cisco.com".lstrip("w.")) #cisco.com #en este caso, el método elimina los caracteres especificados en su argumento que se encuentran al principio

print("pythoninstitute.org".lstrip(".org")) #pythoninstitute.org #no elimina nada porque el org se encuentra al final

print("pythoninstitute.org".lstrip("p")) #ythoninstitute.org #sí elimina la p del principio

#Método replace()
#con dos parámetros devuelve una copia de la cadena original
#en la que todas las apariciones del primer argumento han sido reemplazadas
#por el segundo argumento

print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) #www.pythoninstitute.org
print("This is it!".replace("is", "are")) #Thare are it
print("Apple juice".replace("juice", "")) #Apple 

#si el segundo argumento es una cadena vacía, reemplazar significa realmente eliminar
#si el primer argumento es una cadena vacía, el segundo ocupa su lugar
#replace () con tres parámetros emplea un tercer argumento (un número) para limitar el número re reemplazos
print("This is it!".replace("is", "are", 1)) #Thare is it #Solo reemplaza una vez, la primera
print("This is it!".replace("is", "are", 2)) #Thare are it #reemplaza dos veces

#Método rfind()
#realiza la búsqueda de su argumento comenzando desde el final de la cadena r de reversa
#sin embargo el valor de los índices sigue siendo el miscmo, sólo la primera vez que aparece será considerando el principio de la búsqueda el final de la secuencia
print("tau tau tau".rfind("ta"))    #8
print("tau tau tau".rfind("ta", 9)) #-1 #comienza a buscar desde el índice 9 
print("tau tau tau".rfind("ta", 3, 9)) #4 #comienza a buscar desde el índice 3 hasta el 9 #el valor del índice que arroja es el resultante del conteo desde el índice cero en el rango establecido (3-9)

#Método rstrip()
#r->right afecta desde el lado derecho de la cadena
print("[" + " upsilon ".rstrip() + "]") #[ upsilon]
print("cisco.com".rstrip(".com"))    #cis

#Método split()
#divide la cadena y crea una lista de todas las subcadenas detectadas
#asume que las subcadenas están delimitadas por espacios en blanco
#Los espacios no participan en la operación y no se copian en la lista resultante
#cadena vacía == lista resultante vacía
'''Nota: operación inversa con método join()'''
print("phi         chi\npsi".split()) #['phi,'chi,'psi']

#Método startswith()
#espejo de endswith(), comprueba si una cadena dada COMIENZA con la subcadena especificada
print("omega".startswith("meg")) #False
print("omega".startswith("om")) #True

#método strip()
#combina los efectos causados por rstrip() y lstrip()
#crea una nueva cadena que carece de todos los espacios en blanco INCIALES y FINALEs
print('['+"          aleph   ".strip()+']') #[aleph]

#Método swapcase()
#crea una nueva cadena intercambiando todas las letras por mayúsculas o minpusculas
#dentro de la cadena original: los caracteres mayus turn into minus and viceversa
#todos los demás caracteres permanecen intactos
print("Yo sé que no sé nada.1".swapcase()) #yO SÉ QUE NO SÉ NADA.1

#Método title()
#Cambia la primera letra de CADA palabra a mayúsculas, convirtiendo todas las demás en minus
print('Yo sé que no sé nada.1'.title()) #Yo Sé Que No Sé Nada.1

#Método upper()
#hace una copia de la cadena de origen, reemplaza todas las letras minus con sus equivalentes en mayus
print("Yo sé que no sé nada.2".upper()) #YO SÉ QUE NO SÉ NADA.2

'''Puntos Clave'''
'''
1. Algunos de los métodos que ofrecen las cadenas son:
capitalize(): cambia todas las letras de la cadena a mayúsculas.
center(): centra la cadena dentro de una longitud conocida.
count(): cuenta las ocurrencias de un carácter dado.
join(): une todos los elementos de una tupla/lista en una cadena.
lower(): convierte todas las letras de la cadena en minúsculas.
lstrip(): elimina los caracteres en blanco al principio de la cadena.
replace(): reemplaza una subcadena dada con otra.
rfind(): encuentra una subcadena comenzando por el final de la cadena.
rstrip(): elimina los caracteres en blanco al final de la cadena.
split(): divide la cadena en una subcadena usando un delimitador dado.
strip(): elimina los espacios en blanco iniciales y finales.
swapcase(): intercambia las mayúsculas y minúsculas de las letras.
title(): hace que la primera letra de cada palabra sea mayúscula.
upper(): convierte todas las letras de la cadena en letras mayúsculas.

2. El contenido de las cadenas se puede determinar mediante los siguientes métodos (todos devuelven valores booleanos):

endswith(): ¿La cadena termina con una subcadena determinada?
isalnum(): ¿La cadena consta solo de letras y dígitos?
isalpha(): ¿La cadena consta solo de letras?
islower(): ¿La cadena consta solo de letras minúsculas?
isspace(): ¿La cadena consta solo de espacios en blanco?
isupper(): ¿La cadena consta solo de letras mayúsculas?
startswith(): ¿La cadena consta solo de letras mayúsculas?'''

for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')
#ABC123xyz

s1 = '¿Dónde están las nevadas de antaño?'
s2 = s1.split() #['¿Dónde','están','las','nevadas','de','antaño?']
print(s2[-2]) #de

the_list = ['¿Dónde', 'están', 'las', 'nevadas?']
s = '*'.join(the_list)
print(s) #¿Dónde*están*las*nevadas?

s = 'Es fácil o imposible'
s = s.replace('fácil', 'difícil').replace('im', '')
print(s) #Es difícil o posible

'''Cadenas en acción'''
#Comparando cadenas
#las comparaciones se hacen con los valores de puntos de código
'alpha' == 'alpha' #True
'alpha' != 'Alpha' #False

#comparación de cadenas de diferentes longitudes, cadena más larga mayot
'alpha' < 'alphabet' #True

#la comparación de cadenas distingue entre mayus y minus mayus menores que minus
'beta' > 'Beta' #True

#Si una cadena contiene solo dígitos, no es un número, si se hace una comparación con números arroja TypeError
#ej: '10' == 10 <- TypeError
a ='10' == '010' #False #49 48 == 48 49 48
b = '10' > '010'  #True  #49 48 > 48 49 48 ¿?No entiendo :()
c = '10' > '8'    #False #49 48 > 56
d = '20' < '8'    #True  #50 48 < 56
e = '20' < '80'   #True  #50 48 < 56 48

print(a,b,c,d,e, sep=" ")
print(ord('1')) #49
print(ord('2')) #50
print(ord('8')) #56
print(ord('0')) #48

#Ordenamiento
#ordenar listas que contienen cadenas
#Función sorted(): toma un argumento (una lista) y retorna una nueva lista
#con los elementos ordenados del argumento. La lista original permanece intacta
first_greek = ['omega','alpha','pi','gamma']
first_greek_2 = sorted(first_greek)

print (first_greek) #['omega', 'alpha', 'pi', 'gamma']
print(first_greek_2) #['alpha', 'gamma', 'omega', 'pi']

#Método sort() afecta la lista misma-no se crea una lista nueva
second_greek = ['omega','alpha','pi','gamma']
print(second_greek)

second_greek.sort()
print(second_greek) #continua siendo la misma lista

#¿Cómo convertis un número (int or float) en str y viceversa?
#Función str() conversión de cadena a número
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)
print(si+' '+sf)

#La transformación inversa sóloes posible cuando la cadena representa un número válido
#int() float()

si = '13'
sf='1.3'
itg = int(si)
flt = float(sf)
print(itg+flt) #14.3 se convirtieron en número, --> se realiza la operación matemática

'smith' > 'Smith' #True
'Smiths' < 'Smith' #False
'Smith' > '1000'  #True
'11' < '8'        #True

s1 = '¿Dónde están las nevadas de antaño?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1]) #de #El orden es alfabético! 
print(s3)













