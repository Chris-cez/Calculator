import cpu

class Keyboard:
    def __init__(self, cpu):
        self.cpu = cpu

    def sendValue(self, value, type):
        self.cpu.addDigit(value, type)
        pass