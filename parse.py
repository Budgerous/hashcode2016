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
0 0 0
5 6
1
2
'''


def parse_input_file(file_path):
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

    warehouse_stocks = ['stock of items' for i in range(num_warehouses)]
    warehouse_locations = ['location' for i in range(num_warehouses)]

    warehouse_lines = lines[4:4 + (num_warehouses * 2)]

    j = 0
    for i in range(num_warehouses):
        warehouse_locations[i] = [int(x) for x in warehouse_lines[j].strip().split()]
        warehouse_stocks[i] = [int(x) for x in warehouse_lines[j + 1].strip().split()]
        j += 2

        # print(warehouse_locations[i], "# warehouse_location ", i )
        # print(warehouse_stocks[i], "# warehouse_stock ", i )

    # orders

    num_orders_line = 4 + (num_warehouses * 2)
    num_orders = int(lines[num_orders_line].strip())
    # print(num_orders, "# num_orders")

    order_lines = lines[num_orders_line + 1: num_orders_line + 1 + (num_orders * 3)]
    orders = [['destination', 'volume', 'product types'] for i in range(num_orders)]

    k = 0
    for i in range(num_orders):
        for j in range(3):
            orders[i][j] = [int(x) for x in order_lines[k + j].strip().split()]
        k += 3

        # print(orders[i], "# order ", i )


    return num_rows, num_columns, num_drones, num_turns, max_payload, num_product_types, product_types_weights, num_warehouses, warehouse_stocks, warehouse_locations, num_orders, orders
