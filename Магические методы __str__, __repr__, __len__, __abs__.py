# __str__() - для отображения информации об объекте класса для пользователей
# (например, для функции print, str)

# __repr__() - для отображения информации об объекте класса в режиме отладки (для разработчиков)

# __len__() - позволяет применять функцию len() к экземплярам класса

# __abs__() - позволяет применять функцию abs() к экземплярам класса


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"


cat = Cat('Васька')
print(cat)

# --------------------------------------------------------------------


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, -2, -5)
print(len(p))
print(abs(p))
