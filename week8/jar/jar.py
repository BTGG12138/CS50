class Jar:
    def __init__(self, capacity=12):
        if int(capacity)<0:raise ValueError("capacity应非负")
        self._capacity=int(capacity)
        self._size=0
        #私有变量要加上下划线，反正就是要这样仅赋值
    def __str__(self):
        return "🍪"*self._size
    def deposit(self, n):
        if (self._size+int(n)>self._capacity):raise ValueError("deposit太多了")
        else:self._size+=int(n)                                            
    def withdraw(self, n):
        if (self._size-int(n)<0):raise ValueError("withdraw太多了")
        else:self._size-=int(n)
    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size