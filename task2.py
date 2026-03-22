class Product:
    def __init__(self, name, price, quantity):
        """Ініціалізація атрибутів товару."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        """Обчислює загальну вартість (ціна * кількість)."""
        return self.price * self.quantity

    def display_info(self):
        """Виводить детальну інформацію про товар."""
        total = self.calculate_total_price()
        print(f"--- Інформація про товар ---")
        print(f"Назва: {self.name}")
        print(f"Ціна за одиницю: {self.price} грн")
        print(f"Кількість на складі: {self.quantity} шт.")
        print(f"Загальна вартість: {total} грн")
        print("-" * 28)

laptop = Product("Ноутбук ASUS", 25000, 3)

laptop.display_info()

mouse = Product("Мишка Logitech", 800, 10)
mouse.display_info()
