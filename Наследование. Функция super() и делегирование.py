# расширение, если в базовом классе отсутствует атрибут, который есть в дочернем классе
# переопределение, если в базовом классе присутствует атрибут, который есть в дочернем классе


class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'инициализатор Geom для {self.__class__}')
        self.x1 = x1
        self.y1 = y2
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)  # в нашем случае это эквивалентно Geom.__init__(self, .....)
        print('инициализатор Rect')       # вызов методов базового класса через super - называется делегированием
        self.fill = fill

    def draw(self):
        print("Рисование прямоугольника")


l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)
