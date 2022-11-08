# def create_class_point(name, base, attrs):  # описали простейший метакласс
#     attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
#     return type(name, base, attrs)


class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name, base, attrs)

    # def __init__(cls, name, base, attrs):
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD = 100
    #     cls.MIN_COORD = 0


class Point(metaclass=Meta):
    def get_coords(self):
        return 0, 0


pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())
