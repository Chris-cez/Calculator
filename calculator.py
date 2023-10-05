# class  Keyboard:
#     def __init__(my):
#         my.buttons = []
#         my.adressCPU = None
#     def add_button(my, button):
#         my.buttons.append(button)
#     def del_button(my, button):
#         my.buttons.remove(button)

# class Button:
#     def __init__(my):
#         my.digit = None
#         my.operator = None
#         my.control = None
#         my.adressKeyboard = None
#     def click():
#         pass

# class Screen:
#     def __init__(my, value):
#         my.__visor = value

#     def write(my, value):
#         pass

#     def clear(my):
#         pass

#     def backspace(my):
#         pass

# class CPU:
#     def __init__(my):
#         my.adressScreen = None
#         my.value = int()
#         my.memory1 = int()
#         my.memory2 = int()
#         my.operator = None

#     def operate(my, value, memory, operator):
#         match(operator):
#             case '+':
#                 memory2 =  value + memory
#             case '-':
#                 memory2 =  value - memory
#             case '*':
#                 memory2 =  value * memory
#             case '/':
#                 if memory == 0:
#                     return "Error: division by zero!"
#                 memory2 =  value / memory
#             case _:
#                 return "Error: invalid operator!"
#         return memory2

#     def clearMemory1(my):
#         pass

#     def saveMemory1(my):
#         pass
    
#     def clearMemory2(my):
#         pass

#     def saveMemory2(my):
#         pass
# class Calculator:
#     def __init__(my):
#         pass

#////////////////////////////////////////////////////////////////////////////////////////

class Screen:
    def __init__(self):
        self.display = ""

    def write(self, text):
        self.display += text

    def clear(self):
        self.display = ""

    def backspace(self):
        if self.display:
            self.display = self.display[:-1]


class Button:
    def __init__(self, digit):
        self.digit = digit

    def click(self, screen):
        screen.write(self.digit)


class Keyboard:
    def __init__(self):
        self.adress_cpu = None
        self.digits = [Button(str(i)) for i in range(10)]
        self.operators = [Button("+"), Button("-"), Button("*"), Button("/")]
        self.controls = [Button("="), Button("C"), Button("backspace"), Button("Save memory1"), Button("Save memory2"), Button("Clear memory1"), Button("Clear memory2")]

    def add_digit(self, digit):
        self.adress_cpu.add_digit(digit)

    def add_operator(self, operator):
        self.adress_cpu.add_operator(operator)

    def add_controls(self, control):
        self.adress_cpu.add_controls(control)

    def del_digit(self):
        self.adress_cpu.del_digit()

    def del_operator(self):
        self.adress_cpu.del_operator()

    def del_controls(self):
        self.adress_cpu.del_controls()


class CPU:
    def __init__(self, screen):
        self.adress_screen = screen
        self.operator = ""
        self.value = ""
        self.memory1 = None
        self.memory2 = None

    def save_value_in_memory1(self):
        self.memory1 = self.value
        self.value = ""

    def save_value_in_memory2(self):
        self.memory2 = self.value
        self.value = ""

    def calculate(self):
        if self.operator and self.memory1 and self.value:
            try:
                result = eval(f"{self.memory1}{self.operator}{self.value}")
                self.value = str(result)
                self.memory1 = None
                self.operator = ""
            except ZeroDivisionError:
                self.value = "Error: Division by zero"
            except Exception:
                self.value = "Error: Invalid operation"

    def clear_memory1(self):
        self.memory1 = None

    def clear_memory2(self):
        self.memory2 = None


class Calculator:
    def __init__(self):
        self.screen = Screen()
        self.keyboard = Keyboard()
        self.keyboard.adress_cpu = CPU(self.screen)
        self.cpu = self.keyboard.adress_cpu

    def run(self):
        while True:
            print("Screen:", self.screen.display)
            choice = input("Enter a digit, operator, or control: ")
            if choice == "C":
                self.screen.clear()
                self.cpu.clear_memory1()
                self.cpu.clear_memory2()
                self.cpu.value = ""
                self.cpu.operator = ""
            elif choice == "=":
                self.cpu.calculate()
            else:
                for digit in self.keyboard.digits + self.keyboard.operators + self.keyboard.controls:
                    if choice == digit.digit:
                        digit.click(self.screen)
                        if digit.digit.isdigit():
                            self.cpu.add_digit(digit.digit)
                        elif digit.digit in "+-*/":
                            self.cpu.add_operator(digit.digit)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
