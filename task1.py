import math

def calculator_logic(func):
    def wrapper(*args, **kwargs):
        print("--- Калькулятор активовано (для виходу введіть 'exit') ---")
        while True:
            expression = input("Введіть математичний вираз: ")
            
            if expression.lower() == 'exit':
                print("Завершення роботи калькулятора.")
                break
            
            try:
                result = func(expression)
                print(f"Результат: {result}")
            except ZeroDivisionError:
                print("Помилка: Ділити на нуль неможна.")
            except NameError:
                print("Помилка:таки символи недозволені.")
            except SyntaxError:
                print("Помилка: Неправильний синтаксис виразу.")
            except Exception as e:
                print(f"Непередбачена помилка: {e}")
                
    return wrapper

@calculator_logic
def calculate(expression):
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    return eval(expression, {"__builtins__": None}, allowed_names)

if __name__ == "__main__":
    calculate()
