class Prueba:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return str('El nombre es :{self.nombre}') + str(self.edad)

if __name__ == '__main__':
    a = Prueba ('egla', 25)

    print(a)