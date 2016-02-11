
import math

warehouses = [[0,0], [0,1], [0,2], [1,0], [1,2], [2,0], [2,1], [2,2]]

def distance(self):
    position = [1,1]
    target = self
    return math.sqrt(math.pow(position[0] - target[0], 2) + math.pow(position[1] - target[1], 2))

print(warehouses)
print(warehouses.sort(key=distance))
print(warehouses)
