class Vehicle:

    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money, owner):
        if self.owner is not None:
            return "Car already sold"
        if money >= self.price and self.owner is None:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money-self.price:.2f}"
        return "Sorry, not enough money"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is None:
            return f"{self.model} {self.type} is on sale: {self.price}"
        return f"{self.model} {self.type} is owned by: {self.owner}"


a = 5
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)