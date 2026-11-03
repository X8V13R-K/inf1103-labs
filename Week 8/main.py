from Product import Product
from Inventory import Inventory

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

if __name__ == "__main__":
    main()
