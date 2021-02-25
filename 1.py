class Matrix:
    def __init__(self, data=[]):
        # нет проверки принимаемых значений.
        self.data = data
        self.xlen = len(data[0])
        self.ylen = len(data)

        # максимальная длинна значения в матрице.
        self.max = 0
        for y in self.data:
            # проверка размерности:
            if len(y) != self.xlen:
                raise ValueError
            for x in y:
                # проверка типов
                try:
                    x = int(x)
                except ValueError:
                    raise ValueError

                str_len = len(str(x))
                if str_len > self.max:
                        self.max = str_len

    def __str__(self):
        # никогда так не делать в одну строчку - читаемсть 0.
        # лучше сделать по простому зато код более поддерживаемый.
        return "\n".join([''.join([f'{str(x):>{self.max+1}}' for x in y]) for y in self.data])

    def __add__(self, other):
        # проверить размерость объектов
        if self.xlen != other.xlen or self.ylen != other.ylen:
            raise ValueError
        # можно сделать в одну строчку но читаемость будет хуже
        new = []
        for i1, i2 in zip(self.data, other.data):
            new.append([j1+j2 for j1, j2 in zip(i1, i2)])

        return Matrix(new)

data = [[1,2,3,4], [-500,6,7,8]]
morpheus = Matrix(data)
trinity = Matrix(data)
neo = morpheus + trinity
print(neo)
