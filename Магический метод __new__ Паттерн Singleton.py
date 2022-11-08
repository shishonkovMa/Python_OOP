# __new__() - вызывается перед созданием объекта класса


class Point:
    def __new__(cls, *args, **kwargs):
        print("вызов __new__ для " + str(cls))
        return super().__new__(cls)

    def __init__(self, x, y):
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)


# Паттерн Singleton
class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None
