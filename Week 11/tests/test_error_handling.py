import os
import ast
import glob
import tempfile
import unittest
from unittest.mock import patch
from Supplier import Supplier
from Inventory import Inventory
from input_helpers import get_positive_float
from product_loader import load_products

CSV_TEXT = """product_type,product_id,name,price,stock_quantity
physical,P001,Desk Lamp,25.00,10
digital,D001,Photo Editor,49.90,100
service,S001,Installation,30.00,5
physical,P002,Office Chair,abc,3
physical,P003,Monitor Stand,39.50,7
"""


class TestErrorHandling(unittest.TestCase):
    def setUp(self) -> None:
        # Use a temporary folder so tests never touch your real inventory.json
        self.temp_dir = tempfile.TemporaryDirectory()
        os.environ["INVENTORY_DIR"] = self.temp_dir.name
        self.supplier = Supplier("S001", "TechSupplies Pte Ltd", "sales@techsupplies.sg")
        with patch("builtins.print"):
            self.inventory = Inventory("test_inventory.json")

    def tearDown(self) -> None:
        del os.environ["INVENTORY_DIR"]
        self.temp_dir.cleanup()

    def test_invalid_input_asks_again(self) -> None:
        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]), \
             patch("builtins.print") as mock_print:
            result = get_positive_float("Enter a price: ")
        self.assertEqual(result, 12.5)
        mock_print.assert_any_call("Please enter a valid number, e.g. 12.50")
        mock_print.assert_any_call("Please enter a number greater than zero.")

    def test_missing_file_handled_gracefully(self) -> None:
        with patch("builtins.print") as mock_print:
            load_products("does_not_exist.csv", self.inventory, self.supplier)
        mock_print.assert_any_call("Products file not found: does_not_exist.csv")
        mock_print.assert_any_call("Load attempt finished.")
        self.assertEqual(len(self.inventory.products), 0)

    def test_bad_rows_skipped_and_valid_rows_load(self) -> None:
        csv_path = os.path.join(self.temp_dir.name, "products.csv")
        with open(csv_path, "w") as file:
            file.write(CSV_TEXT)
        with patch("builtins.print") as mock_print:
            load_products(csv_path, self.inventory, self.supplier)
        loaded_ids = [product.product_id for product in self.inventory.products]
        self.assertEqual(loaded_ids, ["P001", "D001", "P003"])
        mock_print.assert_any_call("3 products loaded.")
        mock_print.assert_any_call("Load attempt finished.")

    def test_every_except_is_specific(self) -> None:
        for filename in glob.glob("*.py"):
            with open(filename) as file:
                tree = ast.parse(file.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.ExceptHandler):
                    self.assertIsNotNone(node.type, f"Bare 'except:' found in {filename}")


if __name__ == "__main__":
    unittest.main()
