class Screen:
    def __init__(self):
        self.digits = [None,None,None,None,None,None,None,None]
        self.digitCounter = 0
        self.decimalSeparatorPos = 0

    symbols = [
        ["███","█ █","█ █","█ █","███"],
        ["  █"," ██","█ █","  █","███"],
        ["███","  █","███","█  ","███"],
        ["███","  █"," ██","  █","███"],
        ["█ █","█ █","███","  █","  █"],
        ["███","█  ","███","  █","███"],
        ["███","█  ","███","█ █","███"],
        ["███","  █"," █ "," █ "," █ "],
        ["███","█ █","███","█ █","███"],
        ["███","█ █","███","  █","███"]
    ]

    def setDecimalSeparator(self):
        if self.decimalSeparatorPos == 0:
            self.decimalSeparatorPos = self.digitCounter

    def clear(self):
        self.digits = [None,None,None,None,None,None,None,None]
        self.digitCounter = 0
        self.decimalSeparatorPos = 0
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        self.showDigits()

    def showDigit(self, index, row, col):
        print(self.symbols[index][row],end=" ")
        if row == 5:
            if self.decimalSeparatorPos == col + 1:
                print("▗")

    def showDigits(self):
        i = 0
        cont = 0
        while (i < 5):
            for j in self.digits:
                match j:
                    case "ZERO":
                        self.showDigit(0, i, cont)
                    case "ONE":
                        self.showDigit(1, i, cont)
                    case "TWO":
                        self.showDigit(2, i, cont)
                    case "THREE":
                        self.showDigit(3, i, cont)
                    case "FOUR":
                        self.showDigit(4, i, cont)
                    case "FIVE":
                        self.showDigit(5, i, cont)
                    case "SIX":
                        self.showDigit(6, i, cont)
                    case "SEVEN":
                        self.showDigit(7, i, cont)
                    case "EIGHT":
                        self.showDigit(8, i, cont)
                    case "NINE":
                        self.showDigit(9, i, cont)
                    case _:                        
                        break
                cont += 1
            print()
            i+=1
        print("")
        
    def add(self, digit):
        self.digits[self.digitCounter] = digit
        self.digitCounter += 1
        self.showDigits()