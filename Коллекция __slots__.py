import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):  # Для замера времени
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ('x', 'y')  # 2 разрешенных локальных свойства. Также при __slots__ коллекция __dict__ не формируется
    # Также __slots__ уменьшает объем памяти, занимаемой экземпляром класса, и ускоряет работу с "x", "y"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


p = Point(1, 2)
p2 = Point(1, 2)
print(p.__sizeof__() + p.__dict__.__sizeof__())
print(p2.__sizeof__())

t1 = timeit.timeit(p.calc)
t2 = timeit.timeit(p2.calc)
print(t1, t2)
