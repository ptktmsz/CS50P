class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        new_size = self.size + n
        if new_size <= self.capacity:
            self.size += n
        else:
            raise ValueError("Not enough place for cookies.")

    def withdraw(self, n):
        new_size = self.size - n
        if new_size >= 0:
            self.size -= n
        else:
            raise ValueError("Not enough cookies to withdraw")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Please input a capacity that is a non-negative number.")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar()
    jar.deposit(6)
    print(jar)
    print(f"The jar that I created has {jar.size} cookies in it, and it has a capacity of {jar.capacity}.")
    bigjar = Jar(24)
    bigjar.deposit(24)
    print(bigjar)
    print(f"The second jar is bigger: it has {bigjar.size} cookies in it, and it has a capacity of {bigjar.capacity}.")
    # print("Now I'll try to go over the top in this big jar.")
    # bigjar.deposit(1)
    # print("Now I'll try to subtract more cookies from the jar than there really are there.")
    # bigjar.withdraw(30)

if __name__ == "__main__":
    main()