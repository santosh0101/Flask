class Car:
    def __init__(self, brand, model, year):  # Constructor
        self.brand = brand  # Attribute
        self.model = model
        self.year = year

    def display_info(self):  # Method
        print(f"{self.year} {self.brand} {self.model}")

# Creating an object (Instance)
my_car = Car("Toyota", "Camry", 2022)
# my_car.display_info()  # Output: 2022 Toyota Camry
