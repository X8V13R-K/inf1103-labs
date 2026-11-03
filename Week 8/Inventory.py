import os
import json
from Product import Product

class Inventory: 
    def __init__(self):
        DATA_DIR = os.environ.get("INVENTORY_DIR", os.path.join(os.getcwd(), "Week 8"))
        self.filepath = os.path.join(DATA_DIR, "inventory.json")

        # Load inventory.json if it exists, else return an empty list and create the file
        try:
            with open(self.filepath, "r") as file:
                # Convert dictionaries into Product objects 
                inventory = json.load(file)
                self.products = [ Product( item["product_id"], item["name"], item["price"], item["quantity"] ) for item in inventory ]
            print("inventory.json found\nInventory loaded successfully.\n")

        except FileNotFoundError:
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            with open(self.filepath, "w") as file:
                json.dump([], file)
            print("inventory.json not found, created file.\n")
            self.products = []

        except json.JSONDecodeError:
            print("inventory.json is empty or corrupted. Starting with an empty inventory.\n")
            with open(self.filepath, "w") as file:
                json.dump([], file)
            self.products = []

    def display_all(self):
        if not self.products:
            print("No products in inventory.")
            return
        else: 
            print("Current Inventory:")
            for product in self.products:
                print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def add_product(self, product):
        self.products.append(product)
        self.save_inventory()

    def update_product(self, found_product, new_quantity): 
        found_product.quantity = new_quantity 
        self.save_inventory() 
        
        print(f"Stock updated successfully for {found_product.name}.")

    def search_product(self, product_id):
        #receives product_id as parameter from user input
        for product in self.products: 
            if product.product_id == product_id: 
                print("Product Found:") 
                print(f"ID: {product.product_id}") 
                print(f"Name: {product.name}") 
                print(f"Price: {product.price}") 
                print(f"Quantity: {product.quantity}") 
                return product

        print("Product not found")
        return None

    def save_inventory(self): 
        # Convert Product objects into dictionaries
        inventory_data = [
            {
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity
            }
            for product in self.products
        ]
        
        with open(self.filepath, "w") as file:
            json.dump(inventory_data, file)
        print("Inventory saved successfully to inventory.json.")