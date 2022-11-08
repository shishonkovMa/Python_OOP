# __x1 - режим доступа private (служит для обращения только внутри класса)
# _x1 - режим доступа protected (служит для обращения внутри класса и во всех его дочерних классах)


class Geom:
    __name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'инициализатор Geom для {self.__class__}')
        self._x1 = x1
        self._y1 = y2
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill

    def get_coords(self):
        return (self._x1, self._y1)


r = Rect(0, 0, 10, 20)
r.get_coords()
print(r.__dict__)
