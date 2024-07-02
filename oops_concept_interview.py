class Vehicle:
    # Class variable
    engine_status = "ENGINE STARTED"
    
    def start_engine(self):
        print(self.engine_status)

class Car(Vehicle):
    # Overriding the method in the parent class
    def start_engine(self):
        print(f"The car's {self.engine_status}")

class Bike(Vehicle):
    # Overriding the method in the parent class
    def start_engine(self):
        print(f"The bike's {self.engine_status}")

# Creating objects of Car and Bike
car = Car()
bike = Bike()

# Starting engines
car.start_engine()
bike.start_engine()
