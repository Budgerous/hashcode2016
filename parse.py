from warehouse import Warehouse
from order import Order

'''
example input file:
-------------------
100 100 3 50 500
3
100 5 450
2
0 0
5 1 0
5 5
0 10 2
3
1 1
2
2 0
3 3
3
1 0
5 6
1
2
'''

num_rows = 0
num_columns = 0
num_drones = 0
num_turns = 0
max_payload = 0
num_product_types = 0
product_types_weights = 0
num_warehouses = 0
warehouses = []
num_orders = 0
orders = []


def parse_input_file(file_path):
    global num_rows
    global num_columns
    global num_drones
    global num_turns
    global max_payload
    global num_product_types
    global product_types_weights
    global num_warehouses
    global warehouses
    global num_orders
    global orders

    f = open(file_path, 'r')

    lines = f.readlines()

    # global limits

    num_rows, num_columns, num_drones, num_turns, max_payload = [int(x) for x in lines[0].strip().split()]
    # print(num_rows, num_columns, num_drones, num_turns, max_payload, "# num_rows, num_columns, num_drones, num_turns, max_payload")

    # products

    num_product_types = int(lines[1])
    # print(num_product_types, "# num_product_types")

    product_types_weights = [int(x) for x in lines[2].strip().split()]
    # print(product_types_weights, "# product_types_weights")

    # warehouses

    num_warehouses = int(lines[3])
    # print(num_warehouses, "# num_warehouses")

    warehouses = []

    warehouse_lines = lines[4:4 + (num_warehouses * 2)]

    j = 0
    for i in range(num_warehouses):
        location = [int(x) for x in warehouse_lines[j].strip().split()]
        stocks = [int(x) for x in warehouse_lines[j + 1].strip().split()]
        warehouses.append(Warehouse(i, location, stocks))
        j += 2

    # orders

    num_orders_line = 4 + (num_warehouses * 2)
    num_orders = int(lines[num_orders_line].strip())
    # print(num_orders, "# num_orders")

    order_lines = lines[num_orders_line + 1: num_orders_line + 1 + (num_orders * 3)]
    orders = []

    k = 0
    for i in range(num_orders):
        destination = [int(x) for x in order_lines[k + 0].strip().split()]
        product_amount = [int(x) for x in order_lines[k + 1].strip().split()]
        product_type = [int(x) for x in order_lines[k + 2].strip().split()]
        orders.append(Order(destination[0], destination[1], product_type, product_amount))
        k += 3

        # print(orders[i], "# order ", i )
