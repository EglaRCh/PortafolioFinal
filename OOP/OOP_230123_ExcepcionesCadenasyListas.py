a=10
#b=5 #Al dividir entre cinco, no arroja mensaje de error y ejecuta el código contenido en el blque
b=0 #Al dividir entre cero el bloque atrapará el error y arrpjará el mensaje indicado
try:
    print ('Valor A: ', a)
    print ('Valor B: ', b)
    result = a/b
except ZeroDivisionError:
    print('Nno se puede dividir entre cero')
    print ('revisa los valores de la variable b') #Se puede ingresar más de un mensaje en la excepción

print('Resultado ->', result) 

#Lista 
lista = [1,3,4,5]
try:
    print (lista[6]) #La lista ingresada sólo tiene hasta el índice 3, cualquier índice mayor al ingresado no existe en la lista
except IndexError:
    print('Índice fuera de rango')

a=10
#b=5 #Al dividir entre cinco, no arroja mensaje de error y ejecuta el código contenido en el blque
b=0 #Al dividir entre cero el bloque atrapará el error y arrpjará el mensaje indicado
try:
    print ('Valor A: ', a)
    print ('Valor B: ', b)
    result = a/b
'''except Exception: #Usogenérico '''
#Al colocarlo en un principio todas las excepciones posteriores no van a ejecutarse
'''print('Operación matemática NO aceptada')'''
except ZeroDivisionError:
    print('No se puede dividir entre cero') #Se puede ingresar más de un mensaje en la excepción
  
#se recomienda ir de lo más específico a lo general en las excepciones, colocar el excepto Exception al final
print('Resultado ->', result) 

#En el código puede haber dos errores, 
# el código arroja el primer error y 
# se detiene en el mismo, el segundo, 
# aunque un error, no se identifica






