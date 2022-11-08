# __iter__(self) - получение итератора для перебора объекта
# __next__(self) - переход к следующему значению и его считывание

# a = iter(range(5))
# print(next(a))
# print(next(a))

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


fr = FRange(0, 2, 0.5)
# print(next(fr))  # эквивалент print(fr.__next__())
# print(next(fr))
# print(next(fr))
# print(next(fr))

# Т.к. объект fr выступает в роли итератора, его можно перебрать циклом.
# Однако так работать не будет, т.к. объект fr не является итератором
# Для этого нужно прописать дополнительный магический метод __iter__()
for x in fr:
    print(x)


# ----------------------------------------------------------------------


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr = FRange2D(0, 2, 0.5, 4)
for row in fr:
    for x in row:
        print(x, end=" ")
    print()
