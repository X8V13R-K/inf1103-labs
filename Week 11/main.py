from Inventory import Inventory
from Supplier import Supplier
from ProductFactory import ProductFactory
from input_helpers import get_positive_float

def main() -> None:
    inventory = Inventory()
    supplier = Supplier("S001", "TechSupplies Pte Ltd", "sales@techsupplies.sg")   # default supplier for new products

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
            inventory.display_all_products()
            print()

        elif choice == "2":
            print("Add new Product")
            try:
                product_id = input("Enter product ID: ").strip()
                name = input("Enter product name: ").strip()
                price = get_positive_float("Enter product price: $")
                product_type = input("Enter product type (physical/digital): ").strip().lower()
                quantity = int(input("Enter product quantity: ").strip())

                weight = 0.0
                download_size = 0
                if product_type == "physical":
                    weight = float(input("Enter product weight: ").strip())
                elif product_type == "digital":
                    download_size = int(input("Enter download size (MB): ").strip())

                product = ProductFactory.create(product_type, product_id, name, price,
                                                quantity, supplier, weight, download_size)
                inventory.add_product(product)
                print("\nProduct added. Returning to main menu...\n")

            except ValueError as error:
                print(f"Could not add product: {error}\n")

        elif choice == "3":
            print("Update Stock")
            product_id = input("Enter Product ID to update: ").strip()
            found_product = inventory.find_product(product_id)

            if found_product is not None:
                found_product.display_information()
                new_quantity = int(input(f"Enter new stock quantity for {found_product.name}: ").strip())
                inventory.update_product(found_product, new_quantity)
                print("\nReturning to main menu...\n")
            else:
                print("Product not found.\n")

        elif choice == "4":
            print("Search Product")
            product_id = input("Enter product ID to search: ").strip()
            found_product = inventory.find_product(product_id)

            if found_product is not None:
                found_product.display_information()
                print(found_product.get_fulfillment_info())
            else:
                print("Product not found.")
            print()

        elif choice == "5":
            inventory.save_inventory()
            print("Inventory saved.\n")

        elif choice == "6":
            inventory.save_inventory()
            print("Inventory saved. Program terminated.")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 6.\n")


if __name__ == "__main__":
    main()