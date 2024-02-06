class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity
        self.size = 0


    def __str__(self):
        return self.size * '🍪'


    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many!")
        self.size += n



    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Too little!")
        self.size -= n
        return "Nom Nom"


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = n


jar = Jar()
jar.deposit(6)
jar.withdraw(5)
print(jar)
