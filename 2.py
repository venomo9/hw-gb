from abc import ABC, abstractmethod

class MyAb(ABC):
    @abstractmethod
    def info(self):
        pass
    @abstractmethod
    def rate(self):
        pass


class Wear(MyAb):

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def info(self):
        return self.name

    @property
    def rate(self):
        ret = None
        if self.name == 'coat':
            ret = self.size/6.5 + 0.5
        elif self.name == 'suit':
            ret = self.size*2 + 0.3
        else:
            ret = 0

        return ret


wear1 = Wear('coat', 50)
print(f'for {wear1.name} need {wear1.rate} meters')
