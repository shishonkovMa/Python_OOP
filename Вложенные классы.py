class Women:
    title = 'объект класса для поля title'
    photo = 'объект класса для поля photo'
    ordering = 'объект класса для поля ordering'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        # Если хотим при создании экземпляра класса Women создавать объект класса Meta
        self.meta = self.Meta(user + '@' + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self.access = access
            # Не следует обращаться к атрибутам внешнего класса из вложенного
            # self._t = Women.title

w = Women('root', '12345')
print(w.__dict__)
print(w.meta.__dict__)
