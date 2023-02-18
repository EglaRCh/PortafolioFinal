frec =  [0 for i in range(26)]

with open ('archivo,txt', 'r') as file_var:
    cadena = file_var.read().upper()

    for i in cadena:
        if(i.isalpha()):
            frec[ord(i)-65] += 1


for k in range(len(frec)):
    print(chr(k+65), '->', frec[k])

#Ordenamiento con base en la frecuencia
#Guardar en otro archivo con el mismo nombre concatenada extensión .hist
with open('archivo.hist', 'w') as file_writer:

    maximo = max(frec)

    for i in range (maximo, -1, -1):
        for j in range(len(frec)):
            if(i == frec[j]):
                tmp = (chr(j+65), '->', frec[j]) + '\n'
                file_writer.write(tmp)




