import Father
class Computo(Father.Producto):
    def __init__ (self, marca, tipo, existencias, activo,referencia, nombre, pvp, descripcion):
        self.marca=marca
        self.tipo=tipo 
        self.existencias=existencias
        self.activo=activo
        super().__init__(referencia, nombre, pvp, descripcion)
    
    def __str__ (self):
        string = 'Marca: ' + self.marca
        string += 'Tipo: ' + self.tipo
        string += 'Existencias: ' + str(self.existencias)
        string += 'En venta? ' + self.activo
        return super().__str__() + string

    def incrementar (self, existencias):
            if self.activo == 'Inactivo':
                msg = 'Por el momento el producto se encuentra fuera de venta'
            else:
                self.existencias += existencias
                msg = 'La cantidad de existencias actualizada es: {}'.format(self.existencias)
            return msg

    def decrementar (self, existencias):
            if self.activo == 'Inactivo':
                msg = 'Por el momento el producto se encuentra fuera de venta'
            else: 
                if self.existencias < existencias:
                    msg = 'La cantidad que se quiere decrementar es mayor a las existencias'
                else:
                    self.existencias -= existencias
                    msg = 'La cantidad de existencias actualizada es: {}'.format(self.existencias)
            return msg

    def mostrar (self):
        print('La cantidad total de existencias de este producto es: ', self.existencias)

    def activar (self):
        self.activo =  'Activo'
        return
    