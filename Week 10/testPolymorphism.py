import os
from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory

if os.path.exists("Week 9/inventory_poly.json"):
    os.remove("Week 9/inventory_poly.json")

supplier = Supplier("S001", "TechSupplies Pte Ltd", "sales@techsupplies.sg")
laptop = PhysicalProduct("P001", "Laptop", 1299.00, "physical", 10, supplier, 1.8)
ebook = DigitalProduct("D001", "Python eBook", 29.90, "digital", 100, supplier, 5)

# Both types in the SAME inventory
inventory = Inventory("inventory_poly.json")
inventory.add_product(laptop)
inventory.add_product(ebook)

# ONE loop, NO isinstance(), NO separate loops
print("=== Polymorphism through the Product collection ===")
for product in inventory.products:
    print("----------------------------")
    product.display_information()
    print(product.get_fulfillment_info())