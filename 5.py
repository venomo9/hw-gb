class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f'im a {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'im a {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'im a {self.title}')
    
pen = Pen('pen')
pen.draw()

pencil = Pencil('pencil')
pencil.draw()

handle = Handle('handle')
handle.draw()
