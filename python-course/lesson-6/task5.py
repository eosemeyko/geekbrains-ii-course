class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self): # noqa
        print('Запуск отрисовки')
        # TODO незнаю зачем переопределять всем, я бы добавил в print self.title
        #  чтобы универсально было для всех классов например так:
        # print(f'{self.__class__.__name__}: Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Pen: draw {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Pencil: draw {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Handle: draw {self.title}')


pen = Pen('ballpen')
pen.draw()

pencil = Pencil('kid pencil')
pencil.draw()

handle = Handle('marker')
handle.draw()
