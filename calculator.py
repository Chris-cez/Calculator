import cpu, screen, button, keyboard

display1 = screen.Screen()
cpu1 = cpu.Cpu(display1)
keyboard1 = keyboard.Keyboard(cpu1)
buttonPoint = button.Button("POINT", keyboard1)
buttonZero = button.Button("ZERO", keyboard1)
buttonOne = button.Button("ONE", keyboard1)
buttonTwo = button.Button("TWO", keyboard1)
buttonThree = button.Button("THREE", keyboard1)
buttonFour = button.Button("FOUR", keyboard1)
buttonFive = button.Button("FIVE", keyboard1)
buttonSix = button.Button("SIX", keyboard1)
buttonSeven = button.Button("SEVEN", keyboard1)
buttonEight = button.Button("EIGHT", keyboard1)
buttonNine = button.Button("NINE", keyboard1)

