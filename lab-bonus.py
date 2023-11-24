# Task 1.1
# ООП - это методология программирования, где программы строятся на основе объектов, объединяющих данные и методы.
# Четыре основных принципа ООП - инкапсуляция, наследование, полиморфизм и абстракция - обеспечивают создание более
# чистого и модульного кода.
#
# Инкапсуляция: Скрывает внутреннюю реализацию объекта, предоставляя только необходимый интерфейс. Уменьшает сложность
# кода и делает его более устойчивым.
#
# Наследование: Позволяет создавать новые классы на основе существующих, сокращая дублирование кода и обеспечивая
# структурированность.
#
# Полиморфизм: Объекты одного типа могут использовать одинаковые методы с различной реализацией. Это делает код более
# гибким и устойчивым к изменениям.
#
# Абстракция: Скрывает детали реализации, фокусируясь на ключевых аспектах объекта. Упрощает код и позволяет работать
# на более высоком уровне абстракции.
#
# Все эти принципы совместно способствуют созданию модульного, понятного и масштабируемого кода, что является основой
# эффективной разработки программных систем.


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Book info: Title - {self.title}, Author - {self.author}, isbn - {self.isbn}"


class Car:
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def display_car(self):
        print(f"Make - {self.make}, model - {self.model}, year - {self.year}, color - {self.color}, "
              f"mileage - {self.mileage}km")

    def drive(self, number_of_km):
        self.mileage += number_of_km
        print(f"New mileage = {self.mileage}")


class ElectricCar(Car):
    def __init__(self, make, model, year, color, mileage, battery_size):
        super().__init__(make, model, year, color, mileage)
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Battery - {self.battery_size}%")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, num, description):
        self.products.append({"name": name, "num": num, "description": description})

    def show_inventory(self):
        print("Full Inventory:")
        for i in range(len(self.products)):
            print(f"#{i + 1}. Name - {self.products[i]['name']}, number of product - {self.products[i]['num']}, "
                  f"description - {self.products[i]['description']}")

    def change_num(self, name, new_num):
        for i in range(len(self.products)):
            if self.products[i]['name'] == name:
                self.products[i]['num'] = new_num


def main():
    print("Task 1")
    book_1 = Book("Принцип 80/20", "Ричард Кох", "9-785041-203146")
    book_2 = Book("Продавец обуви", "Фил Найт", "9-785699-981625")
    print(f"Book 1 - {book_1}")
    print(f"Book 2 - {book_2}")

    print(f"\nTask 2")
    print("car_1")
    car_1 = Car("Toyota", "Corolla", 2023, "blue", 5000)
    car_1.display_car()
    print("car_2")
    car_2 = Car("Toyota", "Camry", 2020, "black", 25000)
    car_2.display_car()
    car_2.drive(200)
    car_2.display_car()

    print(f"\nTask 3")
    electro_car = ElectricCar("Tesla", "Model S", 2023, "White", 50000, 80)
    electro_car.display_car()
    electro_car.describe_battery()

    print(f"\nFinal Task")
    invent = Inventory()
    invent.add_product("Bread", 100, "Fresh bread")
    invent.add_product("Water", 30, "Bottle of water 0.5L")
    invent.show_inventory()
    invent.change_num("Water", 60)
    invent.show_inventory()


main()



