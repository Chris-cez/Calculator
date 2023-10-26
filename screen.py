import os

class Screen:
    def __init__(self):
        self.digits = ["ZERO",None,None,None,None,None,None,None]
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
        ["███","█ █","███","  █","███"], 
        ["   ","   ","   ","   ","▗  "]
    ]

    def setDecimalSeparator(self):
        if self.decimalSeparatorPos == 0:
            if self.digits[0] == "ZERO":
                self.digitCounter += 1    
            self.decimalSeparatorPos = self.digitCounter
                
        self.showDigits()

    def clear(self):
        self.digits = [None,None,None,None,None,None,None,None]
        self.digitCounter = 0
        self.decimalSeparatorPos = 0
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        self.showDigits()

    def showDigit(self, index, row, col):
        print(self.symbols[index][row],end=" ")
        if self.decimalSeparatorPos == col + 1:
            print(self.symbols[10][row],end=" ")

    def showDigits(self):
        os.system("clear")
        i = 0
        while (i < 5):
            cont = 0
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
        try:
            if self.digits[0] == "ZERO" and self.digitCounter == 0:
                if digit != "ZERO":
                    self.digits[self.digitCounter] = digit
                    self.digitCounter += 1
            else:
                self.digits[self.digitCounter] = digit
                self.digitCounter += 1
            self.showDigits()
        except:
            pass

    def controlPress(self, value):
        try:
            if value == "POINT":
                self.setDecimalSeparator()
        except:
            pass