class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed      = speed
        self.color      = color
        self.name       = name
        self.is_police  = is_police

        self.is_go      = False
        self.position   = 'north'

    def go(self):
        self.is_go = True

    def stop(self):
        self.is_go = False

    def show_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def turn(self, l_or_r):
        dir = {'north': 1, 'east': 2, 'south': 3, 'west': 4}
        rid = {1: 'north', 2: 'east', 3: 'south', 4: 'west'}
        if l_or_r == 'right':
            pos = dir[self.position]
            pos += 1
            if pos > 4:
                pos = 1
            self.position = rid[pos]
        else:
            pos = dir[self.position]
            pos -= 1
            if pos < 1:
                pos = 4
            self.position = rid[pos]

    def info(self):
        print(f'speed: {self.speed}, color: {self.color}, name: {self.name}, is_police: {self.is_police}, is_go: {self.is_go}, \
position: {self.position}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, max_speed):
        Car.__init__(self, speed, color, name, is_police)
        self.max_speed = max_speed

    def show_speed(self):
        if (self.speed > self.max_speed):
            print('Ur speed is more than max!')
        return self.speed
    
car = Car(speed=60, color='red', name='bmw', is_police=False)
car.go()
car.stop()
car.turn('left')
car.turn('left')
car.turn('left')
car.turn('left')
car.info()
print(car.show_speed())

town = TownCar(speed=65, color='red', name='bmw', is_police=False, max_speed=60)
town.info()
print(town.show_speed())

work = TownCar(speed=65, color='red', name='bmw', is_police=False, max_speed=40)
town.info()
print(town.show_speed())
