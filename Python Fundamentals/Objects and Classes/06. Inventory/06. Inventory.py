class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []
        self.initial_capacity = capacity

    def add_item(self, item):
        if self.__capacity:
            self.__capacity -= 1
            return self.items.append(item)
        return "not enough room in the inventor"

    def get_capacity(self):
        return self.initial_capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity}"


inventory = Inventory(5)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)
