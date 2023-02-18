#Herencia múltiple
class empleado:
    def __init__(self,nombrex,idenx,generox,):
        self.nombre = nombrex
        self.iden = idenx
        self.genero = generox

class Provincia:
    domicilio = 'México'
    colonia = 'Buenavista'

class CodigoPostal:
    def __init__(self, codposx):
        self.codpos=codposx

class CodigoPostal2:
    postal = '06101'

class RecHumanos(empleado, CodigoPostal, Provincia):
    def __init__(self, nombrex, idenx, generox, codposx):
        empleado. __init__(self,nombrex,idenx,generox)
        CodigoPostal.__init__(self,codposx)

    def saludo(self):
        print('Hola, mi nombre es ' + self.nombre + "y mi ID es " + self.iden + ".")
        print('Trabajo en Recursos Humanos')
        if self.genero == 'F':
            print('Género femenino')
        else:
            print('Género masculino')
        print('vivo en ' + self.domicilio + 'en la colonia' + self.colonia + '.')
        print('Código postal: ' + self.codpos)

class Tecnologias(empleado, Provincia, CodigoPostal):
    def saludo (self):
        print('Hola, mi nombre es ' + self.nombre + "y mi ID es " + self.iden + ".")
        print('Trabajo en Tecnologías de la Información')
        if self.genero == 'F':
            print('Género femenino')
        else:
            print('Género masculino')
        print('vivo en ' + self.domicilio + 'en la colonia' + self.colonia + '.')
        print('Código postal: ' + self.codpos)

class Marketing (empleado, Provincia):
    def saludo (self):
        print('Hola, mi nombre es ' + self.nombre + "y mi ID es " + self.iden + ".")
        print('Trabajo en Marketing')
        if self.genero == 'F':
            print('Género femenino')
        else:
            print('Género masculino')
        print('vivo en ' + self.domicilio + 'en la colonia' + self.colonia + '.')
        
empleado1 = RecHumanos('Karla', '182052', 'F', '06100')
empleado1.saludo()

print('*******************')

empleado2 = Tecnologias('Pedro', '182053', 'M', '06101')
empleado2.saludo()

print('*******************')

empleado3 = RecHumanos('Carlos', '182054', 'M', '06102')
empleado3.saludo()

print('*******************')

empleado4 = Tecnologias('Kenia', '182055', 'F', '06103')
empleado4.saludo()

print('*******************')

empleado5 = Marketing('Pamela', '182056', 'F')
empleado5.saludo()

print('*******************')

