import json


def write_order_to_json(item, quantity, price, buyer, date):
    orders_data = dict()
    with open('orders.json', 'r') as json_file:
        orders_data = json.load(json_file)
    if not 'orders' in orders_data:
        orders_data['orders'] = []

    orders_data['orders'].append({
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    })
    with open('orders.json', 'w') as json_file:
        json.dump(orders_data, json_file, indent=4)


for i in range(10):
    write_order_to_json(f'Product#{i}', 4*i, 100*i, 'Roman', '12-10-2020')
