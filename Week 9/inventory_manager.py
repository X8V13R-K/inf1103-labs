import os
import json

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight): 
        super().__init__(product_id, name, price, quantity)
        self.weight = weight

    def display_information(self):
        print(f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Weight: {self.weight}")

        
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, download_size): 
        super().__init__(product_id, name, price, quantity)
        self.download_size = download_size

    def display_information(self):
        print(f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Download size: {self.download_size}MB")

product1 = DigitalProduct("P001", "Laptop", 1200.00, 15, 25000)

product1.display_information()

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



def main():
    inventory = Inventory()
    while True:
        print("=========================================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("=========================================================\n")
        print("----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------\n")

        choice = input("Enter option: ").strip()
        if choice == "1":
            inventory.display_all()
            print()

        elif choice == "2":
            print("Add new Product")
            product_id = input("Enter product ID: ").strip()
            name = input("Enter product name: ").strip()
            price = float(input("Enter product price: ").strip())
            quantity = int(input("Enter product quantity: ").strip())
            product = Product(product_id, name, price, quantity)

            inventory.add_product(product)
            print("\nReturning to main menu...\n")

        elif choice == "3":
            print("Update Stock")
            product_id = input("Enter Product ID to update: ").strip()

            # Search for product first
            found_product = inventory.search_product(product_id)

            #If product is found, carry on with updating
            if found_product is not None: 
                new_quantity = int( input( f"Enter new stock quantity for {found_product.name}: " ).strip() )
                inventory.update_product(found_product, new_quantity)
                print("\nReturning to main menu...\n")

        elif choice == "4":
            print("Search Product")
            product_id = input("Enter product ID to search: ").strip()

            inventory.search_product(product_id)
            print()

        elif choice == "5":
            inventory.save_inventory()
            print()

        elif choice == "6":
            print("Saving inventory and exiting the program.")
            inventory.save_inventory()
            print("Inventory saved successfully.")
            print("Thank you for using the Inventory Management System. \nProgram terminated.")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 6.")
            print()
"""
if __name__ == "__main__":
    main()
"""