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
    if not inventory:
        print("No products in inventory.")
    else:
        print("\nCurrent Inventory:")
        for product in inventory:
            print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}, Quantity: {product['quantity']}")
    print()

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
    print("Update Stock")
    product_id = input("Enter Product ID to update: ").strip()
    found_product = next((product for product in inventory if product["id"] == product_id), None)
    
    if found_product:
        print("Product Found: ")
        print(f"Name: {found_product['name']} \nQuantity: {found_product['quantity']}")
        new_quantity = int(input(f"Enter new stock quantity for {found_product['name']}: ").strip())
        found_product["quantity"] = new_quantity
        saveInventory(inventory)
        print(f"Stock updated successfully for {found_product['name']}.")
    else:
        print("Product not found.")

def searchProduct():
    print("Search Product")
    product_id = input("Enter Product ID to search: ").strip()
    if product_id:
        found_product = next((product for product in inventory if product["id"] == product_id), None)
        if found_product:
            print("Product Found: ")
            print("-----------------------------")
            print(f"ID: {found_product['id']} \nName: {found_product['name']} \nPrice: ${found_product['price']:.2f} \nQuantity: {found_product['quantity']}")
            print("-----------------------------")
        else:
            print("Product not found.")

def saveInventory(inventory):
    with open(filepath, "w") as file:
        json.dump(inventory, file)
    print("Inventory saved successfully to inventory.json.")



inventory = load_inventory()
displayMenu()