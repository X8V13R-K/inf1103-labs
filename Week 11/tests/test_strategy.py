import unittest
from Supplier import Supplier
from ProductFactory import ProductFactory
from Order import Order
from NoDiscount import NoDiscount
from PercentageDiscount import PercentageDiscount
from BulkDiscount import BulkDiscount
from StudentDiscount import StudentDiscount


class TestStrategy(unittest.TestCase):
    def setUp(self) -> None:
        supplier = Supplier("S001", "TechSupplies Pte Ltd", "sales@techsupplies.sg")
        chair = ProductFactory.create("physical", "P001", "Office Chair", 125.00, 10, supplier, weight=5.0)
        self.order = Order("O001")
        self.order.add_order_line(chair, 2)          # lines add up to 250

    def test_default_is_no_discount(self) -> None:
        self.assertEqual(self.order.calculate_total(), 250)

    def test_each_strategy_gives_correct_total(self) -> None:
        cases = [
            (NoDiscount(), 250),
            (PercentageDiscount(10), 225),
            (BulkDiscount(200, 20), 230),
            (StudentDiscount(), 237.5),
        ]
        for strategy, expected in cases:
            self.order.set_discount(strategy)
            self.assertAlmostEqual(self.order.calculate_total(), expected)

    def test_bulk_discount_not_applied_below_threshold(self) -> None:
        self.order.set_discount(BulkDiscount(500, 20))
        self.assertEqual(self.order.calculate_total(), 250)

    def test_set_discount_changes_existing_order(self) -> None:
        self.order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(self.order.calculate_total(), 230)
        self.order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(self.order.calculate_total(), 225)

    def test_order_has_no_discount_if_elif(self) -> None:
        with open("Order.py") as file:
            source = file.read()
        for name in ["PercentageDiscount", "BulkDiscount", "StudentDiscount"]:
            self.assertNotIn(name, source)            # Order never names a specific discount
        self.assertNotIn("discount_type", source)


if __name__ == "__main__":
    unittest.main()
