class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.fila = []

    def put (self, elem):
        self.fila.insert(0, elem)

    def get (self):
        if len(self.fila) > 0:
            elem = self.fila[-1]
            del self.fila[-1]
            return elem
        else:
            raise QueueError

class SuperQueue (Queue):
    def __init__(self):
    
        super().__init__()   
    def isempty (self) :
        self.fila == []

            
        
    


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)

for i in range(4):
    try:
        if not que.isempty():
            print(que.get())
    except QueueError:
        print('Cola vacía')
