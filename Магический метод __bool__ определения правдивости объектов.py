# __len__() - вызывается функцией bool(), если не определен магический метод __bool__()
# __bool__() - вызывается в приоритетном порядке функцией bool()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        return self.x == self.y


p = Point(10, 10)
if p:
    print('Объект p дает True')
else:
    print('Объект p дает False')
