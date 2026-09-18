def get_valid_input(): 
    deliveryAmt = 0
    unitsProcessed = 0
    numFailedEntrys = 0

    while True:
        amt = input("Stock Quantity:")

        if amt.isdigit(): 
            #Valid input
            amt = int(amt)
            deliveryAmt = process_delivery(deliveryAmt, amt)
            print ("Tax for this delivery is: $" + str(calculate_tax(amt)))

            unitsProcessed += 1

            if deliveryAmt > 500: 
                #Delivery amount exceeds 500
                print("Warning: Delivery amount exceeds 500.")
                break

        elif amt.lower() == "quit":
            #User quit
            print("Deliveries processed:", unitsProcessed)
            print("Failed entries:", numFailedEntrys)
            break

        else:
            #Invalid input 
            numFailedEntrys += 1
            print("Invalid input. Please enter a valid positive number.")


def process_delivery(deliveryAmt, amt):
    deliveryAmt = deliveryAmt + amt
    return deliveryAmt

def calculate_tax(amt):
    tax_rate = 0.10  # 10% tax rate
    tax_amount = amt * tax_rate
    return tax_amount

def generate_report(total_units, failed_attempts):
    ...

get_valid_input()