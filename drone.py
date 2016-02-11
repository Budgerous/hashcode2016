import math

class Drone:
    'they fly'
    max_load = 0
    x = 0
    y = 0
    quantity = []

    def __init__(self, x, y, max_load, n_types):
        self.x = x
        self.y = y
        self.max_load = max_load
        self.quantity = [0 for x in range(n_types)]

    def move(self, newX, newY):
        self.x = newX
        self.y = newY

    def getCost(self, newX, newY):
        return math.sqrt(math.pow(self.x - newX, 2) + math.pow(self.y - newY,2))

    def getAmountOfType(self, type):
        return self.quantity[type]

    def load(self, type, amount):
        self.quantity[type] += amount

    def deliver(self, x, y, type, amount):
        self.move(x, y)
        self.quantity[type] -= amount

    def unload(self, x, y, type, amount):
        self.move(x, y)
        self.quantity[type] -= amount
