def load_inventory():
    try: 
        file = open("Week 4/inventory.txt", "r")
        inventory = file.readlines()
        file.close()
        return inventory

    except FileNotFoundError:
        file = open("Week 4/inventory.txt", "w")
        file.close()
        inventory = []
        return inventory

def save_inventory(history):
    file = open("Week 4/inventory.txt", "a")
    for item in history:
        file.write(item + "\n")
    file.close()
    print("New orders saved to inventory.txt")

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

inventory = load_inventory()
get_valid_input(inventory)