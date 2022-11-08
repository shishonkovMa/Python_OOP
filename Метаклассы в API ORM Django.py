class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'


# вышенаписанный код фактически заменяет ниженаписанный


class Women:
    class_attrs = {'title': 'заголовок', 'content': 'контент', 'photo': 'путь к фото'}
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'

    def __init__(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value


w = Women()
print(w.__dict__)
