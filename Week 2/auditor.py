inventory = 0
unitsProcessed = 0
numFailedEntrys = 0
while True:
    qty = input("Stock Quantity:")

    if qty.isdigit(): 
        #Valid input
        inventory += int(qty)
        unitsProcessed += 1
        #print("Inventory:", inventory)

        if inventory > 500: 
            #Inventory count exceeds 500
            print("Warning: Inventory exceeds 500 units.")
            break

    elif qty.lower() == "quit":
        #User quit
        print("Units processed:", unitsProcessed)
        print("Failed entries:", numFailedEntrys)
        break

    else:
        #Invalid input 
        numFailedEntrys += 1
        print("Invalid input. Please enter a valid positive number.")