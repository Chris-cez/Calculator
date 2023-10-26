import keyboard

class Button:
    def __init__(self, value, keyboard):
        self.value = value
        self.keyboard = keyboard
        match value:
            case "ONE":
                self.type = "digit"
            case "TWO":
                self.type = "digit"
            case "THREE":
                self.type = "digit"
            case "FOUR":
                self.type = "digit"
            case "FIVE":
                self.type = "digit"
            case "SIX":
                self.type = "digit"
            case "SEVEN":
                self.type = "digit"
            case "EIGHT":
                self.type = "digit"
            case "NINE":
                self.type = "digit"
            case "ZERO":
                self.type = "digit"
            case "POINT":
                self.type = "control"
            case _:
                self.type = "Invalid"
            

    def press(self):
        self.keyboard.sendValue(self.value, self.type)
