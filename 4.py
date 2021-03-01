class Store:

    def __init__(self, address):
        self.address = address


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

