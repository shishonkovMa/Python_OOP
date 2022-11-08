# __init__(self) - инициализатор объекта класса
# __del__(self) - финализатор класса (вызывается перед уничтожением экземпляра класса

class Point:
    color = 'red'
    circle = 2

    # Магический метод __что-то__
    def __init__(self, x, y):  # делает сразу при объявлении класса
        self.x = x
        self.y = y
    # def __init__(self, x=0, y=0):  можно делать даже так,
    # тогда при вызове не надо описывать параметры: pt = Point()

    def __del__(self):
        print("Удаление экземпляра: " + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point(1, 2)
print(pt.__dict__)
