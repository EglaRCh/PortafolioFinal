class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0

    def push (self, val):
        val = 1
        self.__count += val
        Stack.push(self, val)

    def get_counter(self):
        return self.__count
        

    def pop(self):
        Stack.pop (self)
        
	
stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
