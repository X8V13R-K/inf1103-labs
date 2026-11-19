import unittest
from Supplier import Supplier
from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from ProductFactory import ProductFactory


class TestFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier("S001", "TechSupplies Pte Ltd", "sales@techsupplies.sg")

    def test_creates_physical_product(self) -> None:
        product = ProductFactory.create("physical", "P001", "Desk Lamp", 25.00, 10, self.supplier, weight=1.2)
        self.assertIsInstance(product, PhysicalProduct)
        self.assertIsInstance(product, Product)

    def test_creates_digital_product(self) -> None:
        product = ProductFactory.create("digital", "D001", "Photo Editor", 49.90, 100, self.supplier, download_size=500)
        self.assertIsInstance(product, DigitalProduct)
        self.assertIsInstance(product, Product)

    def test_unknown_type_raises_clear_error(self) -> None:
        with self.assertRaises(ValueError) as context:
            ProductFactory.create("service", "S001", "Installation", 30.00, 5, self.supplier)
        self.assertIn("Unknown product type: service", str(context.exception))

    def test_products_not_created_directly(self) -> None:
        for filename in ["main.py", "Inventory.py"]:
            try:
                with open(filename) as file:
                    source = file.read()
            except FileNotFoundError:
                continue
            self.assertNotIn("PhysicalProduct(", source, filename)
            self.assertNotIn("DigitalProduct(", source, filename)


if __name__ == "__main__":
    unittest.main()
