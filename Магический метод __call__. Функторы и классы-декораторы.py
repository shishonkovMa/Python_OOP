# dunder-методы (double underscope) = магические методы
# Благодаря __call__ мы можем вызывать класс подобно функции
import math


class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    # Благодаря прописи __call__ мы можем вызывать экземпляр класса подобно функции: c()
    # Классы, которые себя так ведут, называются функторы
    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')
        return args[0].strip(self.__chars)  # удаляем из начала и конца строки все символы,
                                            # которые находятся в __chars


s1 = StripChars("?:!.; ")
res = s1(" Hello World! ")
print(res)


# -----------------------------------------------------------------------------------------
# Теперь реализуем декоратор, но на уровне класса


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x+dx) - self.__fn(x)) / dx


def df_sin(x):
    return math.sin(x)


df_sin = Derivate(df_sin)
print(df_sin(math.pi/3))

# или идентично, но как декоратор:


@Derivate
def df_sin(x):
    return math.sin(x)


print(df_sin(math.pi/3))
