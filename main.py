import parse

possible_orders = []
position = [0, 0]

def distance(self):
    target = self
    return math.sqrt(math.pow(position[0] - target[0], 2) + math.pow(position[1] - target[1], 2))

#list all warehouses by distance from order destination k
def best_warehouses(o):
    position = o.position
    return sorted(warehouses, distance)
    

#does this warehouse have the required items for this order?
def is_possible(o, w):
    return True

#sort orders by possible and impossible
def sort_orders():
    for o in orders:
        l = best_warehouses(o)
        print(l);

        # for w in l:
        #     if(is_possible(o, w)):

        #         possible_orders.append()
        #         orders.remove(o)


def main():
    file_path = "input.txt"
    input.parse_input_file(file_path)

    sort_orders()

if __name__ == "__main__":
    main()