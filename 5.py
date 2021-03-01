class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Store:

    def __init__(self, address):
        self.address = address
        self.device = {}

    def push(self, device, count):
        if self.device.get(device):
            self.device[device] += count
        else:
            self.device[device] = count

    def pull(self, address, device, count):
        # c адресом даже не работаем.
        if self.device.get(device) >= count:
            self.device[device] -= count
        else:
            raise OwnError('Нельзя извлечь из склада больше устройств чем там есть')


    def info(self):
        print(self.device)


class Device:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Printer(Device):

    def __init__(self, brand, model, is_color):
        Device.__init__(self, brand, model)
        self.is_color = is_color


class Scaner(Device):

    def __init__(self, brand, model, type):
        Device.__init__(self, brand, model)
        self.type = type


class Copier(Device):

    def __init__(self, brand, model, format):
        Device.__init__(self, brand, model)
        self.format = format


store = Store('большая 22')
store.push('printer', 3)
store.push('printer', 3)
store.pull('большая 19', 'printer', 10)
store.info()
