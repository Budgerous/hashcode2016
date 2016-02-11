import input


possible_orders = []


def distance(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1],2))

#list all warehouses by distance from order destination k
def best_warehouses(o):
    return []

#does this warehouse have the required items for this order?
def is_possible(o, w):
    return True

#sort orders by possible and impossible
def sort_orders():
    for o in orders:
        l = best_warehouses(o)

        for w in l:
            if(is_possible(o, w)):

                possible_orders.append()
                orders.remove(o)


def main():
    file_path = "input.txt"
    input.parse_input_file(file_path)
    


if __name__ == "__main__":
    main()