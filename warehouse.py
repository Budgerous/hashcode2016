class Warehouse:

    def __init__(self, id, position, stocks):
        self.id = id
        self.position = position
        self.stocks = stocks

    def get_id(self):
        return self.id

    def get_x(self):
        return self.position[0]

    def get_y(self):
        return self.position[1]

    def get_stocks(self):
        return self.stocks