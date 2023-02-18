def mysplit (strng) :
    b=0
    lista=[]
    for i in range(len(strng)) :
        if strng[i] == ' ' :
            lista.append(strng[b:i])
            b=i+1
        elif (i == len(strng)-1) :
            lista.append(strng[b:i+1])

    print(lista)

x=str(input('Inserta una cadena con los espacios sustituidos por puntos: '))
mysplit(x)

def mysplit (strng, parametro) :
    b=0
    lista=[]
    for i in range(len(strng)) :
        if strng[i] == ' ' :
            lista.append(strng[b:i])
            b=i+1
        elif (i == len(strng)-1) :
            lista.append(strng[b:i+1])

    print(lista)

x=str(input('Inserta una cadena con los espacios sustituidos por puntos: '))
param = input('Ingresa el parámetro: ')
mysplit(x, param)