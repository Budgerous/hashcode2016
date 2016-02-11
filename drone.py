import math
import parse

#parse.parse_input_file("input.txt")

class Drone:
    'they fly'
    x = 0
    y = 0
    quantity = []
    payload = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.quantity = [0 for x in range(parse.num_product_types)]

    def move(self, newX, newY):
        self.x = newX
        self.y = newY

    def getCost(self, newX, newY):
        return math.sqrt(math.pow(self.x - newX, 2) + math.pow(self.y - newY, 2))

    def getAmountOfType(self, type):
        return self.quantity[type]

    def load(self, x, y, type, amount):
        self.move(x, y)
        self.quantity[type] += amount
        self.payload += amount * parse.product_types_weights[type]

    def deliver(self, x, y, type, amount):
        self.move(x, y)
        self.quantity[type] -= amount
        self.payload -= amount * parse.product_types_weights[type]

    def unload(self, x, y, type, amount):
        self.move(x, y)
        self.quantity[type] -= amount
        self.payload -= amount * parse.product_types_weights[type]

    def can_load(self, type, amount):
        return (self.payload + (amount * parse.product_types_weights[type])) <= parse.max_payload


#a = Drone(0, 0)
#a.load(5, 5, 1, 5)
#print(a.getAmountOfType(1))
