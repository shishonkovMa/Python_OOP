class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

# эквивалент вызовов: Point.set_coords(pt) == pt.set_coords()


pt = Point()  # здесь "pt" - объект / экземпляр класса Point
pt.set_coords(1, 2)
print(pt.get_coords())

# Или можно вызвать иначе

f = getattr(pt, 'get_coords')  # Так как имена методов классов - это тоже атрибуты класса
                               # (просто ведут не на классы, а на функции)
print(f())
