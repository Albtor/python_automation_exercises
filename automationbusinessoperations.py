import pandas as pd
import random


def order_fulfillment_automation():
    inventory = pd.DataFrame({
        'Product': ['Laptop', 'Smartphone', 'Headphones', 'Smartwatch', 'Tablet'],
        'Stock': [10,20,15,30,12],
        'Price': [1000,800,150,250,500]
    })

    def receive_order():
        product = random.choice(inventory['Product'])
        quantity = random.randint(1,5)
        return product, quantity

    product, quantity = receive_order()
    print(f"Received order: {quantity} x {product}")

    def check_inventory():
        product_stock = inventory[inventory['Product'] == product]['Stock'].values[0]
        if product_stock <= quantity:
            print(f"Order processed: {quantity} x {product} available in stock")
            return True
        else:
            print(f"insufficient stock: only {product_stock} x {product} available in stock")
            return False

    order_fulfilled = check_inventory(product, quantity)

    def process_order(product, quantity):
        if order_fulfilled:
            print(f"Order processed: {quantity} x {product} for shipping")
            shipping_cost = random.randint(5,20)
            print(f"Shipping cost: ${shipping_cost}")
            print("Order is on the way")
        else:
            print("Order cannot be processed due to insufficient stock")
        process_order(product, quantity)

    def predict_demand(product):
        predicted_demand = random.randint(5,15)
        print(f"Predicted demand for {product}: {predicted_demand}")
        current_stock = inventory[inventory['Product'] == product]['Stock'].values[0]

        if current_stock < predicted_demand:
            print(f"Warning: Stock is insufficient for predicted demand. Consider Restocking")
        else:
            print(f" Stock level is sufficient to meet predicted demand.")

    predict_demand(product)