class Producto:
    def __init__ (self, referencia, nombre, pvp, descripcion):
        self.referencia=referencia
        self.nombre=nombre
        self.pvp=pvp
        self.descripcion=descripcion

    def __str__(self):
        string ='Referencia: ' + self.referencia
        string += '\nNombre del producto: ' + self.nombre
        string += '\n Precio unitario: ' + self.pvp
        string += '\n Descripción: ' + self.descripcion
        return string   

    
