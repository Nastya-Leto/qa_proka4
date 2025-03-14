class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.brand}{self.model}({self.year})"

    def start_engine(self):
        return 'Двигатель запущен'

    def change_year(self, new_year):
        self.year = new_year


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        return 'Электродвигатель запущен'

    def get_battery_info(self):
        return f'Емкость батареи: {self.battery_capacity} кВтч'


auto_nissan = Car('Nissan', ' Note', '2013')
print(auto_nissan.get_description())
print(auto_nissan.start_engine())

auto_tesla = ElectricCar('Tesla', 'S', '2025', '500')
print(auto_tesla.start_engine())
print(auto_tesla.get_battery_info())


class Truck(Car):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def get_load_info(self):
        return f"Грузоподъемность: {self.load_capacity}"


auto_maz = Truck('Kamaz', '65117', '2022', '500')
print(auto_maz.get_load_info())
