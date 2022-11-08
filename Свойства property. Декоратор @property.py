class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old


p = Person('Сергей', 20)
p.set_old(35)
print(p.get_old())

# чтобы не прописывать геттеры и сеттеры для каждого атрибута класса, можно сделать следующее


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)
    # или
    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)


p = Person('Сергей', 20)
print(p.old)

# или


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


p = Person('Сергей', 20)
del p.old
p.old = 5
print(p.__dict__)
