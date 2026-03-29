import colorama
from colorama import Fore, Back, Style
import inspect

# Инициализация библиотеки colorama
# autoreset=True позволяет не писать Style.RESET_ALL после каждой строки
colorama.init(autoreset=True)

def perform_introspection():
    print(f"{Fore.YELLOW}--- Начало интроспекции модуля colorama ---")
    
    # Получаем все атрибуты и методы модуля с помощью функции dir()
    all_attributes = dir(colorama)
    
    print(f"{Fore.CYAN}Список всех найденных атрибутов:{Style.RESET_ALL}")
    print(all_attributes)
    print("\n" + "="*60 + "\n")

    # Выделяем самые важные компоненты по нашему мнению
    # Мы будем использовать словарь для описания каждого важного элемента
    important_components = {
        "Fore": "Этот объект содержит ANSI-последовательности для изменения цвета текста (переднего плана). Например: RED, GREEN, BLUE.",
        "Back": "Этот объект содержит последовательности для изменения цвета фона под текстом.",
        "Style": "Этот объект позволяет управлять стилем текста, например, делать его ярким (BRIGHT) или сбрасывать настройки (RESET_ALL).",
        "init": "Это функция, которая настраивает терминал. На Windows она крайне важна, так как позволяет консоли понимать цветовые коды.",
        "deinit": "Функция, которая останавливает работу colorama и возвращает терминал в исходное состояние."
    }

    print(f"{Fore.GREEN}Анализ ключевых атрибутов и методов:{Style.RESET_ALL}")

    # Проходим циклом по выбранным важным компонентам
    for name, description in important_components.items():
        # Получаем сам объект из модуля по его имени (строке)
        component_object = getattr(colorama, name)
        
        print(f"\n{Fore.MAGENTA}Имя компонента:{Style.RESET_ALL} {name}")
        print(f"{Fore.WHITE}Тип компонента:{Style.RESET_ALL} {type(component_object)}")
        print(f"{Fore.WHITE}Описание работы:{Style.RESET_ALL} {description}")

        # Если это один из классов стилизации, покажем, что внутри него
        if name in ["Fore", "Back", "Style"]:
            # Убираем системные атрибуты (те, что начинаются на __)
            sub_elements = [item for item in dir(component_object) if not item.startswith("_")]
            print(f"{Fore.BLUE}Доступные константы в {name}:{Style.RESET_ALL} {', '.join(sub_elements)}")

    print("\n" + "="*60)
    print(f"{Fore.RED}Демонстрация работы после интроспекции:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Текст стал зеленым, {Fore.YELLOW}а этот - желтым.")
    print(f"{Back.RED}{Fore.WHITE}Белый текст на красном фоне{Style.RESET_ALL}")

# Запуск функции
if __name__ == "__main__":
    perform_introspection()
