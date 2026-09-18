inventory = 0
deliveriesProcessed = 0
numFailedEntrys = 0
while True:
    qty = input("Stock Quantity:")

    if qty.isdigit(): 
        #Valid input
        inventory += int(qty)
        deliveriesProcessed += 1
        #print("Inventory:", inventory)

        if inventory > 500: 
            #Inventory count exceeds 500
            print("Warning: Inventory exceeds 500 units.")
            break

    elif qty.lower() == "quit":
        #User quit
        print("Deliveries processed:", deliveriesProcessed)
        print("Failed entries:", numFailedEntrys)
        break

    else:
        #Invalid input 
        numFailedEntrys += 1
        print("Invalid input. Please enter a valid positive number.")

def get_valid_input(): 
    ...

def process_delivery(current_total, new_value):
    ...

def calculate_tax(amount):
    ...

def generate_report(total_units, failed_attempts):
    ...
