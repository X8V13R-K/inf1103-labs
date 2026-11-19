from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Order import Order
# Note: we never import OrderLine, because only Order creates them

supplier = Supplier("S001", "TechSupplies Pte Ltd", "sales@techsupplies.sg")
laptop = PhysicalProduct("P001", "Laptop", 1299.00, "physical", 10, supplier, 1.8)
ebook = DigitalProduct("D001", "Python eBook", 29.90, "digital", 100, supplier, 5)

# 1. Order creates its own lines
order1 = Order("O001")
order1.add_order_line(laptop, 2)
order1.add_order_line(ebook, 3)
print("--- Order 1 ---")
order1.display_order()

# 2. Same product in a different order
order2 = Order("O002")
order2.add_order_line(laptop, 1)
print("\n--- Order 2 ---")
order2.display_order()

# 3. Predict first: how many OrderLines and Products?
line1 = order1.order_lines[0]
line2 = order2.order_lines[0]
print("\n--- Predict first ---")
print(f"Same OrderLine? {line1 is line2}")                  # False
print(f"Same Product?   {line1.product is line2.product}")  # True

# 4. Remove a line through the Order
print("\n--- Remove a line ---")
order1.remove_order_line("D001")
order1.display_order()

# 5. Delete the order: its lines go with it, the product stays
del order1
print("\n--- After deleting order1 ---")
laptop.display_information()     # Product still exists