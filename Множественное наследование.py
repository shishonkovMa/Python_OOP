class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print('init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")

    def print_info(self):
        print('print_info из MixinLog')


# class MixinLog2:
#     def __init__(self):  # в базовых классах следует прописывать инициализаторы без параметров,
#         super().__init__()  # кроме основного (в нашем случае Goods)
#         print("init MixinLog 2")


class NoteBook(Goods, MixinLog):  # , MixinLog2):
    # если всегда надо, чтобы print_info вызывался из MixinLog:
    def print_info(self):
        MixinLog.print_info(self)


n = NoteBook('Acer', 1.5, 30000)
n.print_info()
# n.save_sell_log()
# print(NoteBook.__mro__)  # method resolution order (порядок вызова классов)


# Если хотим, чтобы print_info вызывался не из первого класса, а именно из MixinLog
# n = NoteBook('Acer', 1.5, 30000)
# MixinLog.print_info(n)
