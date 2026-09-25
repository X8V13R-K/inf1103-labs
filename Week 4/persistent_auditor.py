def load_inventory():
    try: 
        file = open("inventory.txt", "r")
        inventory = file.readlines()
        file.close()
        return inventory

    except FileNotFoundError:
        file = open("Week 4/inventory.txt", "w")
        file.close()
        return []

def save_inventory(inventory):
    ...

def get_valid_input(): 
    if inventory:
        id = int((inventory[-1].split(",")[0]).strip()) + 1
    else:
        id = 1001

    history = []
    while True:
        productName = input("Enter Product Name:").strip()
        if productName.lower() == "quit":
            print("Current Orders: ")
            for orders in inventory:
                print(orders.strip())

            print("New Order Added: ")
            for item in history:
                print(item)
            break

        productQuantity = input("Enter Quantity:").strip()
        if productQuantity.isdigit():
            #Valid input
            productQuantity = int(productQuantity)
            history.append(f"{id}, {productName}, {productQuantity}")
            id += 1

        else:
            #Invalid input 
            print("Invalid input. Please enter a valid positive number.")

def process_delivery(current_total, new_value):
    deliveryAmt = current_total + new_value
    return deliveryAmt

def calculate_tax(amount):
    tax_rate = 0.10  # 10% tax rate
    tax_amount = amount * tax_rate
    return tax_amount

def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed / Rejected Entries:", failed_attempts)

inventory = load_inventory()
get_valid_input()