def get_valid_input(): 
    deliveryAmt = 0
    unitsProcessed = 0
    numFailedEntrys = 0

    while True:
        qty = input("Stock Quantity:")

        if qty.isdigit(): 
            #Valid input
            qty = int(qty)
            deliveryAmt = process_delivery(deliveryAmt, qty)

            unitsProcessed += 1

            print (deliveryAmt)

            if deliveryAmt > 500: 
                #Delivery amount exceeds 500
                print("Warning: Delivery amount exceeds 500 units.")
                break

        elif qty.lower() == "quit":
            #User quit
            print("Deliveries processed:", unitsProcessed)
            print("Failed entries:", numFailedEntrys)
            break

        else:
            #Invalid input 
            numFailedEntrys += 1
            print("Invalid input. Please enter a valid positive number.")


def process_delivery(deliveryAmt, qty):
    deliveryAmt = deliveryAmt + qty
    return deliveryAmt

def calculate_tax(amount):
    ...

def generate_report(total_units, failed_attempts):
    ...

get_valid_input()