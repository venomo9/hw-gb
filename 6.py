class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Store:

    def __init__(self, address):
        self.address = address
        self.device = {}

    @staticmethod
    def validation(var, var_type):
        error = 0
        try:
            var = var_type(var)
        except:
            print(f'not valid param - {var}')
            error = 1

        return error, var

    def push(self, device, count):
        all_error = 0
        error, device = __class__.validation(device, str)
        all_error += error
        error, count = __class__.validation(count, int)
        all_error += error

        if all_error:
            return all_error

        if self.device.get(device):
            self.device[device] += count
        else:
            self.device[device] = count

        return all_error

    def pull(self, address, device, count):
        all_error = 0
        error, device = __class__.validation(device, str)
        all_error += error
        error, count = __class__.validation(count, int)
        all_error += error
        error, address = __class__.validation(address, str)
        all_error += error

        if all_error:
            return all_error

        # c адресом даже не работаем.
        if self.device.get(device) >= count:
            self.device[device] -= count
        else:
            raise OwnError('Нельзя извлечь из склада больше устройств чем там есть')

        return all_error


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
store.push('printer', '3')
store.pull('большая 19', 'printer', 1)
store.info()
