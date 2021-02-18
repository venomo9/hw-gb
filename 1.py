from time import sleep, ctime

class TrafficLight:

    __color = 'red'

    def running(self):
        tl = { 'red' : 7, 'yellow' : 2, 'green' : 5 }
        while True:
            for color, sleep_time in tl.items():
                TrafficLight.__color = color
                print(f'time: {ctime()}, color: {color}')
                sleep(sleep_time)

tl = TrafficLight()
tl.running()
