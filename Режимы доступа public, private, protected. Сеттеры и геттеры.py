# attribute (без одного или двух подчеркиваний вначале) - публичное свойство (public)

# _attribute (с одним подчеркиванием) - режим доступа protected
#   служит для обращения внутри класса и во всех его дочерних классах

# __attribute (с двумя подчеркиваниями) - режим доступа private
#   служит для обращения только внутри класса

from accessify import private, protected  # декораторы


class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    # @private # после добавления этого декоратора мы можем изменить везде __check_value на check_value
            # и тогда метода класса будут защищены от доступа извне
    @classmethod
    def __check_value(cls, x):  # приватный метод
        return type(x) in (int, float)

    def set_coord(self, x, y):  # сеттер (интерфейсный метод)
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coord(self):  # геттер (интерфейсный метод)
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
# print(pt.__x)  # мы не можем обратиться к этому свойству, т.к. оно приватное
# print(pt._Point__x) # однако все же можем, но так делать не рекомендуется
print(pt.get_coord())
# print(dir(pt))    # какие свойства существуют в экземпляре класса pt

# лучше защитить методы класса от доступа извне поможет модуль accessify
