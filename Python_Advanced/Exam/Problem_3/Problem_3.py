def stock_availability(*args):
    products = args[0]
    action = args[1]
    rest_list = []
    new_inventory = []
    if len(args) > 2:
        for i in range(2, len(args)):
            rest_list.append(args[i])
    if action == 'delivery':
        new_inventory = products + rest_list
    else:
        if rest_list:
            for n in range(len(rest_list)):
                item = str(rest_list[n])
                if item.isdigit():
                    new_inventory = products[int(rest_list[n]):]
                else:
                    if item in products:
                        while item in products:
                            products.remove(item)
                    new_inventory = products
        else:
            new_inventory = products[1:]
    return new_inventory


print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
