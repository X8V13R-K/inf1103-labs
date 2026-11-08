import os
from Supplier import Supplier
from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory

# Start with a clean file
if os.path.exists("Week 9/inventory_lsp.json"):
    os.remove("Week 9/inventory_lsp.json")


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfillment_info())


supplier = Supplier("S001", "TechSupplies Pte Ltd", "sales@techsupplies.sg")
laptop = PhysicalProduct("P001", "Laptop", 1299.00, "physical", 10, supplier, 1.8)
ebook = DigitalProduct("D001", "Python eBook", 29.90, "digital", 100, supplier, 5)

# 1. Same function, both subclasses, no changes needed
print("=== show_product_details() with PhysicalProduct ===")
show_product_details(laptop)
print("\n=== show_product_details() with DigitalProduct ===")
show_product_details(ebook)

# 2. Both work with Inventory's normal operations
print("\n=== Inventory operations ===")
inventory = Inventory("inventory_lsp.json")
inventory.add_product(laptop)
inventory.add_product(ebook)

inventory.update_product(laptop, 15)     # calls update_stock() on a PhysicalProduct
inventory.update_product(ebook, 80)      # calls update_stock() on a DigitalProduct
print(f"Laptop stock: {laptop.quantity}")  # 15
print(f"eBook stock:  {ebook.quantity}")   # 80

print(f"Found laptop? {inventory.find_product('P001') is laptop}")
print(f"Found ebook?  {inventory.find_product('D001') is ebook}")

print()
inventory.display_all_products()