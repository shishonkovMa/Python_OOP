class Geom:
    pass


class Line(Geom):
    pass


g = Geom()
l = Line()
print(issubclass(Line, Geom))  # только для классов
print(isinstance(l, Geom))  # узнать принадлежность атрибута к классу (можем также указывать и классы)


# ----------------------------------------------------------------------------------------------------


class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v)
