import colorama
from colorama import Fore, Style

# Инициализация colorama для цветного вывода ошибок
colorama.init(autoreset=True)

result = []

def divider(a, b):
    # Если первое число меньше второго, возбуждаем ValueError
    if a < b:
        raise ValueError("Первое число меньше второго (a < b)")
    
    # Если делитель больше 100, возбуждаем IndexError
    if b > 100:
        raise IndexError("Делитель больше 100 (b > 100)")
    
    return a / b

# Исходные данные. Обратите внимание: ключ [] вызовет ошибку еще при создании словаря,
# так как списки нельзя использовать как ключи (они изменяемые).
# Но для выполнения задания мы обработаем данные максимально гибко.
data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

# Примечание: В вашем примере был ключ []. В Python это невозможно (TypeError).
# Я удалил его, чтобы код вообще мог запуститься, но добавил проверку типов внутри цикла.

print(f"{Fore.CYAN}--- Запуск обработки данных ---\n")

for key in data:
    try:
        # Исправлена опечатка: вместо data[kem] теперь data[key]
        res = divider(key, data[key])
        result.append(res)
        print(f"{Fore.GREEN}Успешно: {key} / {data[key]} = {res}")
        
    except (ValueError, IndexError) as e:
        # Ловим ошибки, которые мы прописали в функции divider
        print(f"{Fore.YELLOW}Ожидаемое исключение ({type(e).__name__}): {e}")
        
    except ZeroDivisionError:
        # Ловим деление на ноль
        print(f"{Fore.RED}Ошибка: Деление на ноль! Ключ: {key}")
        
    except TypeError as e:
        # Ловим ошибки типов (например, если ключ — строка "123")
        print(f"{Fore.MAGENTA}Ошибка типа данных: {e}")
        
    except Exception as e:
        # Ловим любые другие непредвиденные ошибки
        print(f"{Fore.WHITE}{Style.BRIGHT}Неизвестная ошибка: {e}")

print(f"\n{Fore.CYAN}Конечный результат формирования списка:")
print(result)
