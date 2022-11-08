# __getitem__(self, item) - получение значения по ключу item
# __setitem__(self, key, value) - запись значения value по ключу item
# __delitem__(self, key) - удаление элемента по ключу item


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Индекс должен быть целым неотрицательным числом')
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым неотрицательным числом')
        del self.marks[key]


s1 = Student("Сергей", [5, 5, 3, 2, 5])
print(s1.marks[2])

# Но если хотим получать оценку как s1[2], то прописываем магический метод __getitem__
print(s1[2])

# Если хотим иметь возможность менять оценки студентов s1[2] = 4, пропишем магический метод __setitem__
s1[10] = 4
print(s1.marks)

# Для удаления элемента пропишем магический метод __delitem__
del s1[2]
print(s1.marks)
