import csv
from Inventory import Inventory
from Supplier import Supplier
from ProductFactory import ProductFactory

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.reader(file)
            next(reader) # skips the header row
            for row in reader:
                try:
                    product_type, product_id, name, price, stock_quantity = row
                    product = ProductFactory.create(product_type, product_id, name, float(price), int(stock_quantity), supplier)
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as error:
                    print(f"Skipped row {row}: {error}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")
