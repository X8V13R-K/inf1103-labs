import unittest
from Supplier import Supplier
from ProductFactory import ProductFactory
from Order import Order


class TestValidation(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier("S001", "TechSupplies Pte Ltd", "sales@techsupplies.sg")

    def test_price_must_be_greater_than_zero(self) -> None:
        for bad_price in [0, -10]:
            with self.assertRaises(ValueError):
                ProductFactory.create("physical", "P001", "Lamp", bad_price, 5, self.supplier)

    def test_stock_cannot_be_negative(self) -> None:
        with self.assertRaises(ValueError):
            ProductFactory.create("digital", "D001", "App", 9.90, -1, self.supplier)

    def test_zero_stock_is_allowed(self) -> None:
        product = ProductFactory.create("digital", "D001", "App", 9.90, 0, self.supplier)
        self.assertEqual(product.quantity, 0)

    def test_update_stock_cannot_go_negative(self) -> None:
        lamp = ProductFactory.create("physical", "P001", "Lamp", 25.00, 5, self.supplier)
        with self.assertRaises(ValueError):
            lamp.update_stock(-999)
        self.assertEqual(lamp.quantity, 5)            # unchanged

    def test_order_quantity_must_be_greater_than_zero(self) -> None:
        lamp = ProductFactory.create("physical", "P001", "Lamp", 25.00, 5, self.supplier)
        order = Order("O001")
        for bad_quantity in [0, -2]:
            with self.assertRaises(ValueError):
                order.add_order_line(lamp, bad_quantity)
        self.assertEqual(len(order.order_lines), 0)


if __name__ == "__main__":
    unittest.main()
