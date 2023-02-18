class QueueError (IndexError):
    def __str__ (self):
        string = 'Error de Cola'
        return string


class Queue:
    def __init__(self):
        self.fila = []

    def put (self, elem):
        self.fila.insert(0, elem)

    def get (self):
        if len(self.fila) > 0:
            last = self.fila [-1]
            del self.fila [-1]
            return last
        else:
            QueueError.__str__(self)
    


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
#try:
for i in range(4):
    print(que.get())
#except:
    

