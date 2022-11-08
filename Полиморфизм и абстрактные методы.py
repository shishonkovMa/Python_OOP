# Полиморфизм - это возможность работы с совершенно разными объектами (языка Python) единым образом.


class Geom:
    def get_pr(self):
        # return -1
        # или
        raise NotImplementedError('В дочернем классе должен быть переопределен метод get_pr()')


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w+self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4*self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Если забыли реализовать геттер в одном из классов. Это значительный минус.
    # Что делать чтобы программа продолжала работать?
    # Один из способов - создание базового класса
    
    # def get_pr(self):
    #     return self.a + self.b + self.c


geom = [Rectangle(1, 2), Rectangle(3, 4),
        Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 5, 6)]

for g in geom:
    # print(g.get_rect_pr())  # вызывать отдельно специальный метод под нужный класс - не элегантно
    print(g.get_pr())
