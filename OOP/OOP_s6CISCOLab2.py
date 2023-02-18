import os
import os.path

def find(path,dir):
    elementos = os.listdir(path)
    
    for i in elementos:
        ruta =path + '/' + i
        if(os.path.isdir(ruta)):
            if('python' in ruta):
                print(path + '/' + i, '\n')
            find(path + '/' + i, dir_)

find ('.', 'python')