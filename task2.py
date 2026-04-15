import random
import logging
import functools

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s",
    handlers=[
        logging.FileHandler("simulation.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def log_errors(func):
    """Декоратор для логування помилок у методах класу."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Помилка у методі {func.__name__}: {e}", exc_info=True)
            raise e
    return wrapper

class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        logging.info(f"Створено персонажа: {self.name}")

    @log_errors
    def work(self):
        logging.info(f"{self.name} пішов на роботу.")
        self.money += 50
        self.satiety -= 10
        self.gladness -= 5

    @log_errors
    def eat(self):
        logging.info(f"{self.name} обідає.")
        self.satiety += 20
        self.money -= 10

    @log_errors
    def chill(self):
        logging.info(f"{self.name} відпочиває.")
        self.gladness += 15
        self.satiety -= 5

    def is_alive(self):
        if self.satiety < 0:
            logging.critical(f"{self.name} помер від голоду...")
            return False
        if self.gladness < 0:
            logging.warning(f"{self.name} впав у глибоку депресію.")
            return False
        if self.money < -50:
            logging.error(f"{self.name} став банкрутом!")
            return False
        return True

    def live_a_day(self, day_number):
        status = f"День {day_number}: Гроші={self.money}, Ситість={self.satiety}, Радість={self.gladness}"
        logging.info(status)
        
        dice = random.randint(1, 3)
        if self.satiety < 20:
            self.eat()
        elif self.money < 20:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.chill()

if __name__ == "__main__":
    sim_user = Human(name="Nazik")
    
    for day in range(1, 11):
        if not sim_user.is_alive():
            break
        sim_user.live_a_day(day)
        print("-" * 30)

    logging.info("Симуляцію завершено.")
