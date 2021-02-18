class Road:

    depth = 1
    mass  = 25

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def weight(self):
        print(f'вес асфальта: {self._width * self._length * Road.depth * Road.mass}')


road = Road(width=5, length=5)
road.weight()
