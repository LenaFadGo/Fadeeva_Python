class Animal:
    def __init__(self):
        self.age = 0
        self.animal_sound = "..."

class Mammals(Animal):
    def __init__(self):
        super().__init__()
        self.feet_count = 4
        self.eyes_count = 2

class Cats(Mammals):
    def __init__(self):
        super().__init__()
        self.animal_sound = "meow"

    def get_cat_info(self):
        print(f"Коты имеют: {self.feet_count} ног, издают звук: {self.animal_sound}, имеют количество глаз: {self.eyes_count}"
        f"В среднем живут {self.average_age} лет")