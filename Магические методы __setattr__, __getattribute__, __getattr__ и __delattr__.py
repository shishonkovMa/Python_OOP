# __setattr__(self, key, value) - автоматически вызывается при изменении свойства key класса

# __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item

# __getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса

# __delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно: существует оно или нет)


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # @classmethod
    # def set_bound(cls, left):  # тут мы хотим изменить атрибут класса, а не атрибут экземпляра класса
    #     cls.MIN_COORD = left

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError('Доступ запрещен')
        else:
            return object.__getattribute__(self, item)  # класс object, от которого наследуются все классы в python

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError('Недопустимое имя аттрибута')
        else:
            object.__setattr__(self, key, value)
            # или
            # self.__dict__[key] = value
            # но лучше то, что выше

    def __getattr__(self, item):  # если не хотим получать исключение при вызове несуществующего аттрибута
        return False

    def __delattr__(self, item):
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
# a = pt1.y
del pt1.x
print(pt1.__dict__)
# pt1.set_bound(-100)
# print(pt1.__dict__)
# print(Point.__dict__)
