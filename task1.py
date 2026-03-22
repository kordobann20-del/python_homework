import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.progress = 0
        self.gladness = 50
        self.stress = 0
        self.is_alive = True

    def work(self):
        print(f"{self.name} пішов на підробіток.")
        self.money += 50
        self.gladness -= 10
        self.stress += 15

    def study(self):
        print(f"{self.name} готується до сесії.")
        self.progress += 10
        self.stress += 10
        self.money -= 5

    def chill(self):
        print(f"{self.name} відпочиває та витрачає гроші.")
        self.gladness += 20
        self.money -= 30
        self.stress -= 15

    def is_well(self):
        if self.progress < -10:
            print("Відраховано...")
            self.is_alive = False
        elif self.gladness <= 0:
            print("Депресія...")
            self.is_alive = False
        elif self.money < -50:
            print("Банкрут...")
            self.is_alive = False

    def live_a_day(self, day):
        label = f" День {day} з 365 "
        print(f"{label:=^30}")
        
        if self.money < 20:
            self.work()
        elif self.progress < 5:
            self.study()
        elif self.stress > 30:
            self.chill()
        else:
            dice = random.randint(1, 3)
            if dice == 1: self.study()
            elif dice == 2: self.work()
            else: self.chill()

        self.is_well()
        print(f"Гроші: {self.money} | Знання: {self.progress} | Щастя: {self.gladness}")

student = Student("Олексій")
for day in range(1, 366):
    if not student.is_alive:
        break
    student.live_a_day(day)
