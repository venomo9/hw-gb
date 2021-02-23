class Cell:
    def __init__(self, unit):
        # валидируем и сразу приводим к инту.
        self.unit = self.validation(unit)

    def __add__(self, other):
        return Cell(self.unit + other.unit)

    def __mul__(self, other):
        return Cell(self.unit * other.unit)

    def __sub__(self, other):
        if self.unit <= other.unit:
            print('Невозможно произвести вычитание клеток, разность меньше или равно нулю')
            raise ValueError
        else:
            return Cell(self.unit - other.unit)

    def __truediv__(self, other):
        ret = int(self.unit / other.unit)
        if not ret:
            print('Невозможно произвести деление клеток, частное равно нулю')
            raise ValueError
        else:
            return Cell(ret)

    def make_order(self, in_row):
        # валидируем и сразу приводим к инту.
        in_row = self.validation(in_row)
        order = ''

        row = in_row * '*'
        if in_row >= self.unit:
            order = row
        else:
            n = int(self.unit / in_row)
            last = self.unit % in_row

            order = '\\n'.join([row for _ in range(n)])
            if last:
                order = order + '\\n' + last * '*'

        return order

    def info(self):
        print(self.unit)

    def validation(self, val):

        error = 0
        try:
            val = int(val)
            if not val > 0:
                error = 1
        except ValueError:
            error = 1

        if error:
            raise ValueError

        return val


cell1 = Cell(15)
cell2 = Cell(16)

cell3 = cell1 + cell2
cell3.info()

cell4 = cell3 - cell2
cell4.info()

cell5 = cell4 * cell3
cell5.info()

cell6 = cell5 / cell4
cell6.info()

print(cell6.make_order(10))
