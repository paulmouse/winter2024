class Fibonacci:
    def __init__(self):
        self.value = 0
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.value += self.value+1
        self.index += 1
        return self.value

fib = Fibonacci()
for _ in range(10):
    print(next(fib), end = ' ')