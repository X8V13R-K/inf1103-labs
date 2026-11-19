import os
import json
from Product import Product
from Supplier import Supplier
from ProductFactory import ProductFactory


class Inventory:
    def __init__(self, filename: str = "inventory.json") -> None:
        data_dir = os.environ.get("INVENTORY_DIR", os.path.join(os.getcwd(), "Week 10"))
        self.filepath: str = os.path.join(data_dir, filename)
        self.products: list[Product] = []
        self.load_inventory()

    def load_inventory(self) -> None:
        try:
            with open(self.filepath, "r") as file:
                inventory = json.load(file)

            suppliers: dict[str, Supplier] = {}   # reuse ONE object per supplier
            for item in inventory:
                s = item["supplier"]
                if s["supplier_id"] not in suppliers:
                    suppliers[s["supplier_id"]] = Supplier(
                        s["supplier_id"], s["name"], s["contact_email"])
                supplier = suppliers[s["supplier_id"]]

                self.products.append(ProductFactory.create(item["type"], item["product_id"], item["name"], item["price"], item["quantity"], supplier, weight=item.get("weight", 0.0), download_size=item.get("download_size", 0)))
            print(f"{self.filepath} loaded successfully.\n")

        except FileNotFoundError:
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            self.save_inventory()
            print(f"{self.filepath} not found, created file.\n")

        except json.JSONDecodeError:
            print("File is empty or corrupted. Starting with an empty inventory.\n")
            self.save_inventory()

    def display_all_products(self) -> None:
        if not self.products:
            print("No products in inventory.")
            return
        print("Current Inventory:")
        for product in self.products:
            print("----------------------------")
            product.display_information()
            print(product.get_fulfillment_info())

    def add_product(self, product: Product) -> None:
        self.products.append(product)
        self.save_inventory()

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)
        if product is None:
            print("Product not found.")
            return
        self.products.remove(product)    # removes the REFERENCE only
        self.save_inventory()
        print(f"{product.name} removed from inventory.")

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def update_product(self, product: Product, new_quantity: int) -> None:
        product.update_stock(new_quantity - product.quantity)
        self.save_inventory()
        print(f"Stock updated successfully for {product.name}.")

    def save_inventory(self) -> None:
        inventory_data = [product.to_dict() for product in self.products]
        with open(self.filepath, "w") as file:
            json.dump(inventory_data, file, indent=2)