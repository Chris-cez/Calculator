class  Keyboard:
    def __init__(my):
        my.buttons = []
        my.adressCPU = None
    def add_button(my, button):
        my.buttons.append(button)
    def del_button(my, button):
        my.buttons.remove(button)

class Button:
    def __init__(my):
        my.digit = None
        my.operator = None
        my.control = None
        my.adressKeyboard = None
    def click():
        pass

class Screen:
    def __init__(my, value):
        my.__visor = value

    def write(my, value):
        pass

    def clear(my):
        pass

    def backspace(my):
        pass

class CPU:
    def __init__(my):
        my.adressScreen = None
        my.value = int()
        my.memory1 = int()
        my.memory2 = int()
        my.operator = None

    def operate(my, value, memory, operator):
        match(operator):
            case '+':
                memory2 =  value + memory
            case '-':
                memory2 =  value - memory
            case '*':
                memory2 =  value * memory
            case '/':
                if memory == 0:
                    return "Error: division by zero!"
                memory2 =  value / memory
            case _:
                return "Error: invalid operator!"
        return memory2

    def clearMemory1(my):
        pass

    def saveMemory1(my):
        pass
    
    def clearMemory2(my):
        pass

    def saveMemory2(my):
        pass
class Calculator:
    def __init__(my):
        pass
    
#////////////////////////////////////////////////////////////////////////////

# class Teclado:
#     def __init__(my):
#         pass
    
#     def obter_entrada(my):
#         memory2 =  input("Digite um número ou operador: ")


# class Botao:
#     def __init__(my, valor):
#         my.valor = valor
    
#     def clicar(my):
#         memory2 =  my.valor


# class Tela:
#     def __init__(my):
#         pass
    
#     def mostrar_resultado(my, resultado):
#         print(f"Resultado: {resultado}")


# class Cpu:
#     def __init__(my):
#         my.valor1 = None
#         my.valor2 = None
#         my.operador = None
    
#     def receber_entrada(my, entrada):
#         if my.valor1 is None:
#             my.valor1 = float(entrada)
#         elif my.operador is None:
#             my.operador = entrada
#         else:
#             my.valor2 = float(entrada)
    
#     def calcular(my):
#         if my.operador == '+':
#             memory2 =  my.valor1 + my.valor2
#         elif my.operador == '-':
#             memory2 =  my.valor1 - my.valor2
#         elif my.operador == '*':
#             memory2 =  my.valor1 * my.valor2
#         elif my.operador == '/':
#             if my.valor2 == 0:
#                 memory2 =  "Erro: Divisão por zero!"
#             memory2 =  my.valor1 / my.valor2
#         else:
#             memory2 =  "Operador inválido!"


# class Calculadora:
#     def __init__(my):
#         my.teclado = Teclado()
#         my.tela = Tela()
#         my.cpu = Cpu()
    
#     def executar(my):
#         while True:
#             entrada = my.teclado.obter_entrada()
#             if entrada == 'q':
#                 break
#             if entrada in ['+', '-', '*', '/']:
#                 my.cpu.receber_entrada(entrada)
#             else:
#                 try:
#                     my.cpu.receber_entrada(entrada)
#                     resultado = my.cpu.calcular()
#                     my.tela.mostrar_resultado(resultado)
#                 except ValueError:
#                     print("Erro: Entrada inválida!")

# if __name__ == "__main__":
#     calculadora = Calculadora()
#     calculadora.executar()