class Point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x*x + y*y)**0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


pt = Point2D(1, 2)
print(pt.length)

# ----------------------------- Теперь про наследование -----------------------------


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):  # не наследует коллекцию __slots__
    # __slots__ = ()  # если пропишем пустым, то будут разрешены только параметры 'x', 'y' из Point2D
    # __slots__ = 'z',  # если хотим добавить еще один разрешенный локальный атрибут
    # (обязательна висячая запятая, т.к. является первым элементом кортежа)
    pass


pt3 = Point3D(10, 20)
pt3.z = 30
print(pt3.__dict__)