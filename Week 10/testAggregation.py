from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from Inventory import Inventory

supplier = Supplier("S001", "TechSupplies Pte Ltd", "sales@techsupplies.sg")

# 1. Product exists BEFORE any inventory
laptop = PhysicalProduct("P001", "Laptop", 1299.00, "physical", 10, supplier, 1.8)
print("--- Product created on its own ---")
laptop.display_information()

inventory_a = Inventory("inventory_a.json")
inventory_b = Inventory("inventory_b.json")

# 2. Add to A
inventory_a.add_product(laptop)
print(f"\nIn A? {inventory_a.find_product('P001') is not None}")

# 3. Predict first: remove from A, does the product still work?
inventory_a.remove_product("P001")
print(f"In A after removal? {inventory_a.find_product('P001') is not None}")
print("\n--- Product still usable after removal ---")
laptop.display_information()

# 4. Transfer the SAME object to B
inventory_b.add_product(laptop)
print(f"\nSame object in B? {inventory_b.find_product('P001') is laptop}")