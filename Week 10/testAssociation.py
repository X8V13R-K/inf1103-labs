from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

# Supplier is created independently, BEFORE any product
supplier = Supplier("S001", "TechSupplies Pte Ltd", "sales@techsupplies.sg")

# Same supplier object passed into both products (association)
laptop = PhysicalProduct("P001", "Laptop", 1299.00, "Physical", 10, supplier, 1.8)
ebook = DigitalProduct("D001", "Python eBook", 29.90, "Digital", 100, supplier, 5)

print("--- Supplier info through each product ---")
laptop.supplier.display_information()
print()
ebook.supplier.display_information()

print("\n--- Same supplier object? ---")
print(f"laptop.supplier is ebook.supplier: {laptop.supplier is ebook.supplier}")  # True
print(f"laptop.supplier is supplier: {laptop.supplier is supplier}")              # True
print(f"laptop is supplier: {laptop is supplier}")                                # False

print("\n--- Predict first: delete the supplier variable ---")
del supplier
laptop.display_information()
print()
ebook.supplier.display_information()
print("\nProducts still reach the supplier after 'del supplier'")