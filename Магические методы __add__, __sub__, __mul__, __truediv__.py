# __add__() - для операции сложения
# __sub__() - для операции вычитания
# __mul__() - для операции умножения
# __truediv__() - для операции деления
# А также (__floordiv__() - //) и (__mod__() - %)


class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целыми числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")  # для того чтобы строка была: 04, если у нас имеется просто 4

    def __add__(self, other):  # other - значение, которое стоит справа от оператора "+"
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):  # Если экземпляр класса Clock будет записан справа от оператора сложения
        return self + other

    def __iadd__(self, other):  # Если хотим реализовать операнд "+=".
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектов класса Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds += sc
        return self


c1 = Clock(1000)
# Если хотим увеличить время на 100 секунд
c1.seconds = c1.seconds + 100
# Но было бы здорово просто писать c1 = c1 + 100. Для этого мы прописываем метод __add__()
c1 = 100 + c1
c1 += 100
print(c1.get_time())


# Также было бы здорово складывать два экзмепляра класса
c1 = Clock(1000)
c2 = Clock(2000)
c3 = c1 + c2
print(c3.get_time())
