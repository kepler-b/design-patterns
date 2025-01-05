class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f"car is being driven by {self.driver.name}")

class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age < 18:
            print("Driver is too young to drive.")
        else:
            self._car.drive()

class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def execute():
    driver = Driver("John", 19)
    car = CarProxy(driver)
    car.drive()
