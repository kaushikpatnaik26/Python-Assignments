class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")

vehicle = Vehicle("Toyota", "Corolla")
car = Car("Honda", "Civic", 4)

vehicle.display_info()
car.display_info()
