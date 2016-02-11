
class Order:
    destinationX = 0
    destinationY = 0
    product_type = 0
    product_amount = 0

    def __init__(self, destinationX, destinationY, product_type, product_amount):
        self.destinationX = destinationX
        self.destinationY = destinationY
        self.product_type = product_type
        self.product_amount = product_amount

    def getDestination(self):
        return (self.destinationX, self.destinationY)

    def getProductType(self):
        return self.product_type

    def getProductAmount(self):
        return self.product_amount

    def getDestinationX(self)
        return self.destinationX

    def getDestinationY(self)
        return self.destinationY
        
        