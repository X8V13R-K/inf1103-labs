import json
import os

filepath = os.path.join(os.getcwd(), "Week 5", "inventory.json")

print("=========================================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("=========================================================\n")

def load_inventory():
    # Load inventory.json if it exists, else return an empty list and create the file
    try:
        with open(filepath, "r") as file:
            inventory = json.load(file)
        print("inventory.json found\nInventory loaded successfully.\n")
        return inventory
        
    except FileNotFoundError:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as file:
            json.dump([], file)
        print("inventory.json not found, created file.\n")
        return []

    except json.JSONDecodeError:
        print("inventory.json is empty or corrupted. Starting with an empty inventory.\n")
        with open(filepath, "w") as file:
            json.dump([], file)
        return []

def displayMenu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------\n")

    while True:
        choice = input("Enter option: ").strip()
        if choice == "1":
            displayAllProducts()
        elif choice == "2":
            addProduct()
        elif choice == "3":
            updateStock()
        elif choice == "4":
            searchProduct()
        elif choice == "5":
            saveInventory(inventory)
        elif choice == "6":
            print("Saving inventory and exiting the program.")
            saveInventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using the Inventory Management System. \nProgram terminated.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")

def displayAllProducts():
    ...

def addProduct():
    print ("Add New Product")
    product_id = input("Product ID: ").strip()
    product_name = input("Product Name: ").strip()
    product_price = float(input("Price: ").strip())
    product_quantity = int(input("Stock Quantity: ").strip())

    # Adding product to inventory
    inventory.append({
        "id": product_id,
        "name": product_name,
        "price": product_price,
        "quantity": product_quantity
    })
    saveInventory(inventory)
    print("Product added successfully.")

def updateStock():
    ...

def searchProduct():
    ...

def saveInventory(inventory):
    with open(filepath, "w") as file:
        json.dump(inventory, file)
    print("Inventory saved successfully to inventory.json.")



"""
def save_inventory(history):
    file = open("Week 5/inventory.json", "w")
    json.dump(history, file)
    file.close()
    print("New orders saved to inventory.json")

def get_valid_input(inventory): 
    if inventory:
        id = int((inventory[-1].split(",")[0]).strip()) + 1
    else:
        id = 1001

    history = []
    while True:
        productName = input("Enter Product Name:").strip()
        if productName.lower() == "quit":
            print("Current Orders: ")
            if inventory:
                for item in inventory:
                    print(item.strip())
            else:
                print("No orders in inventory.")

            print("New Order Added: ")
            if history:
                for item in history:
                    print(item.strip())
                save_inventory(history)
            else:
                print("No new orders added.")
            break

        productQuantity = input("Enter Quantity:").strip()
        while not productQuantity.isdigit() or int(productQuantity) <= 0:
            print("Invalid input. Please enter a valid positive number.")
            productQuantity = input("Enter Quantity:").strip()

        productQuantity = int(productQuantity)
        history.append(f"{id}, {productName}, {productQuantity}")
        id += 1

"""

inventory = load_inventory()
displayMenu()