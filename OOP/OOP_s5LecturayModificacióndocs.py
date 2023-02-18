while True:
    id= input ('Indica ID: ')
    nombre = input('Indica Nombre: ')
    apellido = input('Indica Apellido: ')

    cad = id + "|" + nombre + "|" + apellido + "\n"

    file = open ('Agenda.txt', 'a+')

    file.write (cad)
    file.close

    continuar = input ('Deseas agregar otro registro?: s(si)/n(No)')