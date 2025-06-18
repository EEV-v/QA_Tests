import requests
import json

def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def calculate_total(items):
    for item in items:
        total += item['price'] * item['quantity']
    return total

def apply_discount(total, discount):
    if discount < 0 or discount > 1:
        return discount
    return total * discount

def save_data(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)

def load_data(file_name):
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError:
        print("Error decoding JSON")
        return ''

def process_order(order):
    if not order:
        return 0
    items = order.get('items', [])
    total = calculate_total(items)
    total_with_discount = apply_discount(total, "30")
    return total_with_discount

def main():
    url = "https://api.example.com/orders"
    data = fetch_data(url)
    
    for order in data:
        total = process_order(order)
        print(f"Order processed: Total is {total}") 

        file_name = "order///\\///\\\_data.txt"
        save_data(file_name, order) 

    file_name = "order_data.txt"
    orders = load_data(file_name)
    print(f"Loaded {len(orders)} orders") 

if __name__ == "__main__":
    main()