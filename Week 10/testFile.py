import os
import inspect
from Supplier import Supplier
from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from Order import Order
from OrderLine import OrderLine


def check(description: str, condition: bool) -> None:
    print(f"[{'PASS' if condition else 'FAIL'}] {description}")


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfillment_info())


# Start from clean files so leftover data from old runs can't affect results
for name in ["test_a.json", "test_b.json"]:
    path = os.path.join("Week 9", name)
    if os.path.exists(path):
        os.remove(path)

supplier = Supplier("S001", "TechSupplies Pte Ltd", "sales@techsupplies.sg")
laptop = PhysicalProduct("P001", "Laptop", 1299.00, "physical", 10, supplier, 1.8)
ebook = DigitalProduct("D001", "Python eBook", 29.90, "digital", 100, supplier, 5)


print("\n=== 1. Association: Supplier and Product ===")
check("Product stores a reference to its Supplier", laptop.supplier is supplier)
check("Both products share ONE Supplier object", laptop.supplier is ebook.supplier)
check("Supplier and Product are separate objects", laptop is not supplier)
del supplier
check("Products still reach the Supplier after 'del supplier'",
      laptop.supplier.name == "TechSupplies Pte Ltd")


print("\n=== 2. Aggregation: Inventory and Product ===")
inventory_a = Inventory("test_a.json")
inventory_b = Inventory("test_b.json")
inventory_a.add_product(laptop)
check("Product added to Inventory A", inventory_a.find_product("P001") is laptop)
inventory_a.remove_product("P001")
check("Product removed from Inventory A", inventory_a.find_product("P001") is None)
check("Product still usable after removal", laptop.get_fulfillment_info() != "")
inventory_b.add_product(laptop)
check("SAME Product object transferred to Inventory B", inventory_b.find_product("P001") is laptop)


print("\n=== 3. Composition: Order and OrderLine ===")
order1 = Order("O001")
order1.add_order_line(laptop, 2)
order1.add_order_line(ebook, 3)
check("Order created its own OrderLines", len(order1.order_lines) == 2)
check("Order total is calculated from its lines (2598.00 + 89.70)",
      round(order1.calculate_total(), 2) == 2687.70)

order2 = Order("O002")
order2.add_order_line(laptop, 1)
line1 = order1.order_lines[0]
line2 = order2.order_lines[0]
check("Each Order has its OWN OrderLine", line1 is not line2)
check("OrderLine refers to the Product without copying it", line1.product is line2.product is laptop)

order1.remove_order_line("D001")
check("OrderLine removed through the Order", len(order1.order_lines) == 1)
del order1
check("Product survives after its Order is deleted", laptop.name == "Laptop")


print("\n=== 4. Type hints ===")
for cls in [Supplier, Product, PhysicalProduct, DigitalProduct, Inventory, Order, OrderLine]:
    missing = [name for name, method in inspect.getmembers(cls, inspect.isfunction)
               if "return" not in method.__annotations__]
    check(f"{cls.__name__}: every method has a return type hint", not missing)


print("\n=== 5. LSP: both subclasses work as a Product ===")
inventory_b.add_product(ebook)
inventory_b.update_product(laptop, 15)
inventory_b.update_product(ebook, 80)
check("update_stock() works the same for PhysicalProduct", laptop.quantity == 15)
check("update_stock() works the same for DigitalProduct", ebook.quantity == 80)
check("get_fulfillment_info() returns a str for both",
      isinstance(laptop.get_fulfillment_info(), str) and isinstance(ebook.get_fulfillment_info(), str))
print("\nshow_product_details() with each type:")
show_product_details(laptop)
show_product_details(ebook)


print("\n=== 6. Polymorphism through the Product collection ===")
for product in inventory_b.products:          # ONE loop, no isinstance()
    print(f"{type(product).__name__}: {product.get_fulfillment_info()}")
check("Physical product runs its own version", "shipping" in laptop.get_fulfillment_info())
check("Digital product runs its own version", "digitally" in ebook.get_fulfillment_info())