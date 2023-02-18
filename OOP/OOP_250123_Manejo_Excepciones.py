'''a=10
b=5
result = 0
lista= [1,3,4,5]
try:
    #result = a/b
    #print(lista[6]) #IndexError
    a-10*2+a      
    #f=open('Empleados.txt') #para que el código pueda leer el archivo, y no arroje error de archivo no encontrado, 
    #es necesario que se encuentre en la misma carpeta en donde se está guardando todo el código
    #print (lista(6))

except ZeroDivisionError: #particular
    print ('No se puede divitir entre cero')
except IndexError:
    print('Fuera de rango')
except FileNotFoundError:
    print('Archivo no encontrado')
except TypeError:
    print('Error de tipo')
except Exception: #para todas las excepeciones
    print('Error no especificado')
else:             #determina qué ejecución generar cuando no entró ninguna excepción
    print('Ejecución completada')
finally:          #siempre se va a ejecutar
    print('M&M')'''

#-------------------    

def division (val1,val2):   
#Se puede ingresar a una función!

    result=0

    try:
        result = val1 / val2

    except ZeroDivisionError: #particular
        print ('No se puede divitir entre cero')
    except IndexError:
        print('Fuera de rango')
    except FileNotFoundError:
        print('Archivo no encontrado')
    except TypeError:
        print('Error de tipo')
    except Exception: #para todas las excepeciones
        print('Error no especificado')

    if result == 0:  
        result = 0
    return result

division (3,5)
#division (3,0) #ZeroDivisionError

#cómo trabajar para poder leer un archivo de excel

try: 
    f = open('Empleados.txt') 
    #Cuando no se especifica la ruta donde físicamente se encuentre 
    # f = open ('C:/base/Empleados.txt') #ruta especificada
    # o se agrega en la carpeta en donde se está trabajando es un error FileNotFoundError
except FileNotFoundError:
    print('El fichero no existe')
else:
    print(f.read())


import pandas as pd 
try:
    f = pd.read_excel('Datos.xlsx')
except FileNotFoundError:
    print('El fichero no existe')
else:
    print(f.head())



