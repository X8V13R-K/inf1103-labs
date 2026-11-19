from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier

class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float, quantity: int, supplier: Supplier, weight: float = 0.0, download_size: int = 0) -> Product:
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, product_type, quantity, supplier, weight)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, product_type, quantity, supplier, download_size)
        else:
            raise ValueError(f"Unknown product type: {product_type}")
