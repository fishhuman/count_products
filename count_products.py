def count_products(data):
    products = {}
    for line in data:
        name, count = line.split(' ')
        count = int(count)
        if name in products:
            products[name] += 1
        else:
            products[name] = count

    return products

data = ['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']
print(count_products(data))                    

