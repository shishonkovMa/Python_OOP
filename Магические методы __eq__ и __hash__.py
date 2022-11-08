# если хэши не равны, то объекты точно не равны
# равные хэши не гарантируют равенство объектов
# если объекты равны, то и их хэши тоже равны

# хэши можно вычислять только для неизменяемых объектов
# print(hash((1,2,3)))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):  # мы подменили вычисление хэша объекта Point на вычисление хэша от координат точки
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)

# print(hash(p1), hash(p1), sep='\n')
print(p1 == p2)

d = {}
d[p1] = 1
d[p2] = 2
print(d)
