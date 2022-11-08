class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod  # работает только с атрибутами класса
    def validate(cls, arg):  # cls - ссылка на текущий класс Vector
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):  # имеет доступ и к экземплярам класса, и к атрибутам класса
        self.x = self.y = 0
        # if Vector.validate(x) and Vector.validate(y):  # Имя класса можно заменять на self:
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_coord(self):  # имеет доступ и к экземплярам класса, и к атрибутам класса
        return self.x, self.y

    @staticmethod  # полностью независимая функция
    def norm2(x, y):
        return x*x + y*y


v = Vector(1, 2)
res = v.get_coord()
# Или:
# res = Vector.get_coord(v)
print(res)

print(Vector.norm2(5, 6))
