import screen

class Cpu:
    def __init__(self, screen):
        self.screen = screen

    def addDigit(self, value, type):
        if type == "digit":
            self.screen.add(value)
        elif type == "control":
            self.screen.controlPress(value)

    def clear(self):
        self.screen.clear()

    def getScreen(self):
        return self.screen