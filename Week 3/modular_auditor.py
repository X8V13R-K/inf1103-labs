def get_valid_input(): 
    deliveryAmt = 0
    numUnitsProcessed = 0
    numFailedEntrys = 0

    while True:
        amt = input("Stock Quantity:")

        if amt.isdigit(): 
            #Valid input
            amt = int(amt)
            deliveryAmt = process_delivery(deliveryAmt, amt)
            print ("Tax for this delivery is: $" + str(calculate_tax(amt)))

            numUnitsProcessed += 1

        elif amt.lower() == "quit":
            #User quit
            generate_report(numUnitsProcessed, numFailedEntrys)
            break

        else:
            #Invalid input 
            numFailedEntrys += 1
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

get_valid_input()