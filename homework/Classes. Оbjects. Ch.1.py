class Automobile:
    def __init__(self, model, year, manufacturer):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.__engine_capacity = ""
        self.__color = ""
        self.__cost = ""

    def get_automobile_info(self):
        info = (f'model = {self.model} \n'
                f'year = {self.year} \n'
                f'color = "{self.__color}')
        print(info)

    def set_engine_capacity(self, engine_capacity):
        self.__engine_capacity = engine_capacity

    def set_color(self, color):
        self.__color = color

    def set_cost(self, cost):
        self.__cost = cost

def get_automobile():
    model = input()
    Lada = Automobile(model=model, year="2012",manufacturer="Russia")
    Lada.set_engine_capacity("350/2")
    Lada.set_color("Black")
    Lada.set_cost("600 000 P")
    Lada.get_automobile_info()

get_automobile()
