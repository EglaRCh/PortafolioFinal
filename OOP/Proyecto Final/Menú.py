import Father, Libro, Alimento, Computo
import sys
lista=[]

opcion = 0
while True :
    print ('\n \nElija su opción:')
    print ('Opción 1: Alta')
    print ('Opción 2: Activar producto')
    print ('Opción 3: Altas de existencias')
    print ('Opción 4: Bajas de existencias')
    print ('Opción 5: Consultar')
    print ('Opción 6: Mostrar todo')
    print ('Opción 0: Salir')
    opcion = input('Ingresa el número de tu elección ')
    
    if opcion == '1' :
        print ('Elija el tipo de producto: ')
        print ('1: Libro')
        print ('2: Alimento')
        print ('3: Computo')
        producto = input('Ingresa el número de tu elección: ')
        if producto == '1': 
            referencia = input('Ingresa la referencia: ')
            nombre = input('Ingresa el nombre del producto: ')
            pvp = input('Ingresa el precio unitario: ')
            descripcion = input('Ingresa la descripción: ')
            isbn = input('Ingresa el ISBN: ')
            autor = input('Ingresa el autor: ')
            existencias = 0
            lista.append(Libro.Libro(isbn, autor, existencias, 'Inactivo', referencia, nombre, pvp, descripcion))
        elif producto == '2': 
            referencia = input('Ingresa la referencia: ')
            nombre = input('Ingresa el nombre del producto: ')
            pvp = input('Ingresa el precio unitario: ')
            descripcion = input('Ingresa la descripción: ')
            productor = input('Ingresa el productor: ')
            distribuidor = input('Ingresa el distribuidor: ')
            existencias = 0
            lista.append(Alimento.Alimento(productor, distribuidor, existencias, 'Inactivo', referencia, nombre, pvp, descripcion))
        elif producto == '3': 
            referencia = input('Ingresa la referencia: ')
            nombre = input('Ingresa el nombre del producto: ')
            pvp = input('Ingresa el precio unitario: ')
            descripcion = input('Ingresa la descripción: ')
            marca = input('Ingresa la marca: ')
            tipo = input('Ingresa el tipo: ')
            existencias = 0
            computo=Computo.Computo(marca, tipo, existencias, 'Inactivo', referencia, nombre, pvp, descripcion)
            lista.append(computo)      

    elif opcion == '2':
        print('Productos disponibles: ')
        for i in range (len(lista)) :
            print (i+1, '->', lista[i])
            print ()
        try:
            producto = int(input ('Ingresa el número de producto elegido: '))
            if producto <= 0 :
                raise ValueError

            lista[producto-1].activar()
            print('Producto activado')
        except ValueError :
            print('Sólo se reciben números mayores a 0')
        except IndexError :
            print('Producto no existente, favor de ingresar un número que se encuentre en la lista')
        
    elif opcion == '3':
        print('Productos disponibles: ')
        for i in range (len(lista)) :
            print (i+1, '->', lista[i])
            print ()
        try:
            producto = int(input ('Ingresa el número de producto elegido: '))
            if producto <= 0 :
                raise ValueError

            valor=int(input('¿Cuántas unidades deseas aumentar?'))

            lista[producto-1].incrementar(valor)
           
        except ValueError :
            print('Sólo se reciben números mayores a 0')
        except IndexError :
            print('Producto no existente, favor de ingresar un número que se encuentre en la lista')

    elif opcion == '4':
        print('Productos disponibles: ')
        for i in range (len(lista)) :
            print (i+1, '->', lista[i])
            print ()
        try:
            producto = int(input ('Ingresa el número de producto elegido: '))
            if producto <= 0 :
                raise ValueError
            valor=int(input('¿Cuántas unidades deseas disminuir?'))
            lista[producto-1].decrementar(valor)
           
        except ValueError :
            print('Sólo se reciben números mayores a 0')
        except IndexError :
            print('Producto no existente, favor de ingresar un número que se encuentre en la lista')
    
    elif opcion == '5':
        print('Productos disponibles: ')
        for i in range (len(lista)) :
            print (i+1, '->', lista[i])
            print ()
        try:
            producto = int(input ('Ingresa el número de producto elegido: '))
            if producto <= 0 :
                raise ValueError

            lista[producto-1].mostrar()
           
        except ValueError :
            print('Sólo se reciben números mayores a 0')
        except IndexError :
            print('Producto no existente, favor de ingresar un número que se encuentre en la lista')

    elif opcion == '6':
        print('Productos disponibles: ')
        for i in range (len(lista)) :
            print (i+1, '->', lista[i])
            print ()
    
    elif opcion == '0' : 
        sys.exit()

    else: 
        print('Opción inválida')

