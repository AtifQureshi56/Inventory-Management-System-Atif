import json

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

class Inventory:
    def __init__(self):
        self.products = self.load_inventory()

    def load_inventory(self):
        with open('inventory.json', 'r') as file:
            return json.load(file)

    def save_inventory(self):
        with open('inventory.json', 'w') as file:
            json.dump(self.products, file, indent=4)

    def add_product(self):
        product_id = input("Product ID: ")
        name = input("Name: ")
        category = input("Category: ")
        price = float(input("Price: "))
        stock_quantity = int(input("Stock Quantity: "))
        
        new_product = {
            "product_id": product_id,
            "name": name,
            "category": category,
            "price": price,
            "stock_quantity": stock_quantity
        }
        self.products[product_id] = new_product
        self.save_inventory()
        print(f"Product '{name}' added.")

    def modify_product(self):
        product_id = input("Enter Product ID to modify: ")
        if product_id in self.products:
            name = input("Updated Name: ")
            category = input("Updated Category: ")
            price = float(input("Updated Price: "))
            stock_quantity = int(input("Updated Stock Quantity: "))
            
            self.products[product_id].update({
                "name": name,
                "category": category,
                "price": price,
                "stock_quantity": stock_quantity
            })
            self.save_inventory()
            print(f"Product '{name}' updated.")
        else:
            print("Product not found.")

    def remove_product(self):
        product_id = input("Enter Product ID to remove: ")
        if product_id in self.products:
            del self.products[product_id]
            self.save_inventory()
            print("Product removed.")
        else:
            print("Product not found.")

    def adjust_stock(self):
        product_id = input("Enter Product ID for stock adjustment: ")
        if product_id in self.products:
            adjustment = int(input("Enter quantity to adjust (+/-): "))
            self.products[product_id]["stock_quantity"] += adjustment
            self.save_inventory()
            print("Stock adjusted.")
        else:
            print("Product not found.")

    def show_all_products(self):
        for product in self.products.values():
            print(f"ID: {product['product_id']}, Name: {product['name']}, Category: {product['category']}, Price: ${product['price']}, Stock: {product['stock_quantity']}")

    def search_by_name(self, name):
        found = [p for p in self.products.values() if p['name'].lower() == name.lower()]
        if found:
            for product in found:
                print(product)
        else:
            print("No product found.")

    def filter_stock(self):
        low_stock_products = [p for p in self.products.values() if p['stock_quantity'] < 5]
        for product in low_stock_products:
            print(f"Low Stock - {product['name']}: {product['stock_quantity']} units")
